from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_showtime, name='create_showtime'),
    path('', views.showtime_list, name='showtime_list'),
    path('<str:pk>/edit/', views.edit_showtime, name='edit_showtime'),
    path('<str:pk>/delete/', views.delete_showtime, name='delete_showtime'),
    path('<str:pk>/', views.view_showtime, name='view_showtime'),
]
