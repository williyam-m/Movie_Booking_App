from django.db import models
import uuid
# Create your models here.
class Theatre(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

'''
class Screen(models.Model):
    id = models.AutoField()
    theatre_id = models.IntegerField()
    name = models.CharField(max_length=255)
    ticket_price = models.DecimalField(max_digits=6, decimal_places=2)
    rows = models.IntegerField()
    columns = models.IntegerField()


class ShowTime(models.Model):
    id = models.AutoField()
    screen_id = models.IntegerField()
    theatre_id = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
'''