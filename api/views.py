from django.http import HttpResponse, HttpResponseBadRequest
import requests
import json
from django.views.decorators.csrf import csrf_exempt
from api.models import Place
from api.serializers import LLSerializer, PlaceSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView 



@api_view(["GET"])
def index(request):
    return Response("Welcome, you have succesfully landed to the API!")



def type_checker(latitude, longitute):
    if (not(type(latitude)) == int and not(type(latitude)) ==float) or (not(type(longitute)) == int and not(type(longitute)) == float):
        return False
    return True

class search(GenericAPIView):

    serializer_class = LLSerializer

    @swagger_auto_schema(tags=['Search Place'])
    def post(self, request, *args, **kwargs):
        if request.method != "POST": # Checking the request method
            return Response(json.dumps({'error': 'Invalid request method'}))

        try:

            serializer = LLSerializer(data=request.data)
            if serializer.is_valid():
                print(serializer.data)

            latitude = serializer.data["latitude"]
            longitude = serializer.data["longitude"]

            #API Validation
            if type_checker(latitude, longitude) == False:
                return Response("Error: Wrong latitude or longitude format! Must be integer or float.")



        except Exception as e:
            return Response(json.dumps({'error': 'Invalid request: {0}'.format(str(e))}), content_type="application/json")

        url = "https://api.foursquare.com/v3/places/search?ll={}%2C{}".format(latitude,longitude)

        headers = {
            "accept": "application/json",
            "Authorization": "fsq38jf5s6BtxsM5GasJ/3pdhr7HlOSL2O6cjpiwegCvd90=",
            
        }

        response = requests.get(url, headers=headers) # sending request to foursquare.com

        response_unicode = response.content.decode('utf-8') # Decoding the response
        response_dict = json.loads(response_unicode)

        response_arr = response_dict["results"] 

        if len(response_arr) == 0:
            return Response("Error: No place is found")
        else:
            foundPlaces = list()
            missingValues = 0
            addedPlaces = 0
            # print(response_arr)
            for uniq_response in response_arr: # Traversing through all places that are found
                
                try:
                    dict = {}
                    dict["fsq_id"] = uniq_response["fsq_id"]
                    dict["latitude"] = uniq_response["geocodes"]["main"]["latitude"]
                    dict["longitude"] = uniq_response["geocodes"]["main"]["longitude"]
                    dict["address"] = uniq_response["location"]["formatted_address"]
                    dict["country"] = uniq_response["location"]["country"]
                    dict["region"] = uniq_response["location"]["region"]
                    dict["name"] = uniq_response["name"]
                    
                    foundPlaces.append(dict["name"])

                    # Creating a serializer
                    serializer = PlaceSerializer(data=dict)
                    
                    if serializer.is_valid():                    
                        serializer.save()  # Saving to the database
                    addedPlaces += 1

                except Exception : # Some values such as "address" are missing in some of the data.
                    # traceback.print_exc()
                    missingValues += 1
                
            newly_added = "[INFO] {} places are added to the database, {} place is skipped due to the missing field.".format(addedPlaces,missingValues) #Api validation
            current_status ="[INFO] Database is now have {} places on it.".format(len(Place.objects.all()))


        return HttpResponse("Found places are {}\n{}\n{}".format(foundPlaces,newly_added,current_status))



@api_view(["GET"])
def getDatabaseInfo(request):

    try:
        places = Place.objects.all()
    except Place.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = PlaceSerializer(places, many=True)
        return Response(serializer.data)



@api_view(["DELETE"])
def cleanDatabase(request):
    try:
        places = Place.objects.all()
    except Place.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "DELETE":
        places.delete()
        return Response("Deleted!!")
    else:
        return Response("Wrong request method!")
