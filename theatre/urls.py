from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create/', views.create_theatre, name='create_theatre'),
    path('<str:pk>/update/', views.update_theatre, name='update_theatre'),
    path('<str:pk>/delete/', views.delete_theatre, name='delete_theatre'),
    path('<str:pk>/', views.view_theatre, name='view_theatre'),
]
