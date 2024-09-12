from django.db import models
import uuid
from django.contrib.auth.models import User
from showtime.models import ShowTime

class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    showtime = models.ForeignKey(ShowTime, on_delete=models.CASCADE)
    seats = models.JSONField(default=list)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    booking_datetime = models.DateTimeField(auto_now_add=True)

