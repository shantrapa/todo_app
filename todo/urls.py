from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('toggle/<str:pk>/', views.toggle_complete, name='toggle'),
    path('rename/<str:pk>/', views.rename, name='rename'),
    path('delete/<str:pk>/', views.delete, name='delete'),
]