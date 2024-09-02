from django.db import models
import uuid
# Create your models here.
class Theatre(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
