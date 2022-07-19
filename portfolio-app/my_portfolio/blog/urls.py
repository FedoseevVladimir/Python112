from django.urls import path

from .views import *

urlpatterns = [
    path('myblog/', BlogHome.as_view(), name='myblog'),
]
