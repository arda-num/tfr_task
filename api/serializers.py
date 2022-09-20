from dataclasses import field, fields
from email.policy import default
from rest_framework import serializers
from api.models import Place, LL

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = [
            "id", 
            "fsq_id", 
            "latitude", 
            "longitude", 
            "address",
            "country",
            "region",
            "name"
        ]


class LLSerializer(serializers.ModelSerializer):
    latitude = serializers.FloatField(default=39.89)
    longitude = serializers.FloatField(default=32.77)
    class Meta:
        model = LL
        fields = [
            "latitude", 
            "longitude"
        ]