from django.shortcuts import render

import requests
import json


def my_weather(request):
    app_id = '8a73b5b4fdc04052bdd181728222408'
    city = "Новосибирск"
    url = f'http://api.weatherapi.com/v1/current.json?key={app_id}&q={city}&aqi=no'
    res = requests.get(url).json()
    c_weather = str(res['current']['temp_c'])
    img1 = str(res['current']['condition']['icon'])
    return render(request, 'my_weather/weather.html', {'c_weather': c_weather, 'city': city, 'img1': img1})
