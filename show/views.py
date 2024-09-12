from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from movie.models import Movie
from showtime.models import ShowTime
from theatre.models import Theatre


def show_movie_theatres(request, movieid):
    movie = get_object_or_404(Movie, id=movieid)
    showtimes = ShowTime.objects.filter(movie=movie).order_by('theatre', 'start_date')

    paginator = Paginator(showtimes, 10)  # Show 10 showtimes per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'movie': movie,
        'page_obj': page_obj,
    }
    return render(request, 'show_movie_theatres.html', context)
