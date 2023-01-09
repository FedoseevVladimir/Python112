from django.urls import path
from .views import my_weather

urlpatterns = [
    path('', my_weather, name='my_weather')
]
