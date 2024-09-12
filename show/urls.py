from django.urls import path
from . import views

urlpatterns = [
path('<str:movieid>/', views.show_movie_theatres, name='show_movie_theatres'),
]