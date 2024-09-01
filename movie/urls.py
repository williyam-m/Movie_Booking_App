from django.urls import path
from . import views

urlpatterns = [
    path('view/<str:movieid>', views.movie, name='movie'),
    path('addmovie', views.addMovie, name='addmovie'),
    path('editmovie/<str:movieid>', views.editMovie, name='editmovie'),
    path('deletemovie/<str:movieid>', views.deleteMovie, name='deletemovie'),
    path('bookmark/', views.bookmark, name='bookmark'),
    path('like/', views.like, name='like'),

    path('dashboard', views.dashboard, name='dashboard'),
    path('search', views.searchMovie, name='searchmovie'),
    path('mylist', views.myList, name='mylist'),
    path('latestmovies', views.latestMovies, name='latestmovies'),

]