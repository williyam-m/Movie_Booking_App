from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.utils.dateparse import parse_date
from movie.models import Movie
from showtime.models import ShowTime
from theatre.models import Theatre

from django.contrib.auth.decorators import login_required
from user.views import role_required


@login_required(login_url='signin')
def show_movie_theatres(request, movieid):
    movie = get_object_or_404(Movie, id=movieid)
    filter_date = request.GET.get('filter_date')

    if filter_date:
        showtimes = ShowTime.objects.filter(movie=movie, start_date__date=parse_date(filter_date)).order_by('theatre',
                                                                                                            'start_date')
    else:
        showtimes = ShowTime.objects.filter(movie=movie).order_by('theatre', 'start_date')

    theatres = Theatre.objects.filter(showtime__in=showtimes).distinct()

    paginator = Paginator(showtimes, 10)  # Show 10 showtimes per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'movie': movie,
        'theatres': theatres,
        'page_obj': page_obj,
        'filter_date': filter_date,
    }
    return render(request, 'show_movie_theatres.html', context)
