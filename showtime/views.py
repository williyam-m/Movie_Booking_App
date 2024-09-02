from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import ShowTime
from movie.models import *
from screen.models import *
from datetime import timedelta


def create_showtime(request):
    if request.method == 'POST':
        movie_id = request.POST.get('movie')
        screen_id = request.POST.get('screen')
        start_date = request.POST.get('start_date')

        movie = get_object_or_404(Movie, pk=movie_id)
        screen = get_object_or_404(Screen, pk=screen_id)
        end_date = datetime.fromisoformat(start_date) + timedelta(minutes=movie.duration)

        if ShowTime.objects.filter(screen=screen,
                                   start_date__lt=end_date,
                                   end_date__gt=datetime.fromisoformat(start_date)).exists():
            return HttpResponse("Collision detected!", status=400)

        ShowTime.objects.create(
            movie=movie,
            screen=screen,
            start_date=datetime.fromisoformat(start_date),
            end_date=end_date
        )
        return redirect('showtime_list')

    movies = Movie.objects.all()
    screens = Screen.objects.all()
    return render(request, 'create_showtime.html', {'movies': movies, 'screens': screens})


def showtime_list(request):
    showtimes = ShowTime.objects.all()
    return render(request, 'showtime_list.html', {'showtimes': showtimes})


def edit_showtime(request, pk):
    showtime = get_object_or_404(ShowTime, pk=pk)
    if request.method == 'POST':
        movie_id = request.POST.get('movie')
        screen_id = request.POST.get('screen')
        start_date = request.POST.get('start_date')

        movie = get_object_or_404(Movie, pk=movie_id)
        screen = get_object_or_404(Screen, pk=screen_id)
        end_date = datetime.fromisoformat(start_date) + timedelta(minutes=movie.duration)

        if ShowTime.objects.filter(screen=screen,
                                   start_date__lt=end_date,
                                   end_date__gt=datetime.fromisoformat(start_date)).exclude(pk=pk).exists():
            return HttpResponse("Collision detected!", status=400)

        showtime.movie = movie
        showtime.screen = screen
        showtime.start_date = datetime.fromisoformat(start_date)
        showtime.end_date = end_date
        showtime.save()
        return redirect('showtime_list')

    movies = Movie.objects.all()
    screens = Screen.objects.all()
    return render(request, 'edit_showtime.html', {'showtime': showtime, 'movies': movies, 'screens': screens})


def delete_showtime(request, pk):
    showtime = get_object_or_404(ShowTime, pk=pk)
    if request.method == 'POST':
        showtime.delete()
        return redirect('showtime_list')
    return render(request, 'delete_showtime.html', {'showtime': showtime})


def view_showtime(request, pk):
    showtime = get_object_or_404(ShowTime, pk=pk)
    return render(request, 'view_showtime.html', {'showtime': showtime})
