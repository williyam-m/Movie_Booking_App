from django.urls import path
from . import views

urlpatterns = [
    path('showtime/<str:pk>/', views.book_screen, name='book_screen'),
    path('confirm_booking/<str:showtime_id>/<str:seats>/', views.confirm_booking, name='confirm_booking'),
    path('booking_success/', views.booking_success, name='booking_success'),
]
