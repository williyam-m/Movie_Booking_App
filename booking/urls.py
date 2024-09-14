from django.urls import path
from . import views

urlpatterns = [
    path('user_booking_dashboard/', views.user_booking_list, name='user_booking_list'),
    path('dashboard/', views.booking_list, name='booking_list'),
    path('detail/<uuid:pk>/', views.booking_detail, name='booking_detail'),
    path('delete/<uuid:pk>/', views.booking_delete, name='booking_delete'),

    path('showtime/<str:pk>/', views.book_screen, name='book_screen'),
    path('confirm_booking/<str:showtime_id>/<str:seats>/', views.confirm_booking, name='confirm_booking'),
    path('booking_success/', views.booking_success, name='booking_success'),
]
