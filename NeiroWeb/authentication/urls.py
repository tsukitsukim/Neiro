from django.urls import path, include
from . import views

urlpatterns = [
    path('register', views.index),
    path('register/', views.index)
]