from django.db import models
import uuid

class Place(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fsq_id = models.CharField(max_length=24)
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.TextField(null=True)
    country = models.TextField()
    region = models.TextField()
    name = models.TextField()
    
  
class LL(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()