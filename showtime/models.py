from django.db import models
from movie.models import Movie
from screen.models import Screen
from theatre.models import *
import uuid
# Create your models here.
class ShowTime(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE, blank=True, null = True)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
