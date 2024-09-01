from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.screen_dashboard, name='screen_dashboard'),
    path('create/', views.create_screen, name='create_screen'),
    path('<str:pk>/update/', views.update_screen, name='update_screen'),
    path('<str:pk>/delete/', views.delete_screen, name='delete_screen'),
    path('<str:pk>/view/', views.view_screen, name='view_screen'),
]
