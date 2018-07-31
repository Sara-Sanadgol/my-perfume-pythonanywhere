from django.urls import path
from . import views

urlpatterns = [
    path('', views.perfume, name='perfume'),
]