from django.db import models
import uuid


class Screen(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4)
    theatre_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    ticket_price = models.DecimalField(max_digits=6, decimal_places=2)
    rows = models.IntegerField(default = 26)
    columns = models.IntegerField(default = 100)