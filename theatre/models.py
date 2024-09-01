from django.db import models
import uuid
# Create your models here.
class Theatre(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

'''
class ShowTime(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4)
    screen_id = models.CharField(max_length=255)
    theatre_id = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
'''