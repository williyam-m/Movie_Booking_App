from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_showtime, name='create_showtime'),
    path('dashboard/', views.showtime_list, name='showtime_list'),
    path('<str:pk>/edit/', views.edit_showtime, name='edit_showtime'),
    path('<str:pk>/delete/', views.delete_showtime, name='delete_showtime'),
    path('<str:pk>/', views.view_showtime, name='view_showtime'),
    path('get_screens/<str:theatre_id>/', views.get_screens_by_theatre, name='get_screens_by_theatre'),
]
