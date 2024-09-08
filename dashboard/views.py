from django.shortcuts import render
from django.db.models import Count
from movie.models import Movie
from theatre.models import Theatre
from screen.models import Screen
from showtime.models import ShowTime
from user.models import User

def dashboard(request):
    context = {
        'movies_count': Movie.objects.count(),
        'theatres_count': Theatre.objects.count(),
        'screens_count': Screen.objects.count(),
        'showtimes_count': ShowTime.objects.count(),
        'users_count': User.objects.count(),
    }
    return render(request, 'main-dashboard.html', context)