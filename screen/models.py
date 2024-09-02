from django.db import models
from theatre.models import Theatre
import uuid


class Screen(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, blank=True)
    ticket_price = models.DecimalField(max_digits=6, decimal_places=2)
    rows = models.IntegerField(default=26)
    columns = models.IntegerField(default=100)