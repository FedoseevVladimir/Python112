from django.shortcuts import render, redirect, get_object_or_404
import requests
from .forms import CityForm
from .models import City


def weather(request):
    app_id = '70a0ff2856ce477f92c181314222005'
    # city = 'Москва'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()
    all_cities = []
    for city in cities:
        url = f"http://api.weatherapi.com/v1/current.json?key={app_id}&q={city.name}&aqi=no"
        res = requests.get(url).json()

        try:
            city_info = {
                'city_pk': city.id,
                'city': city.name,
                'temp': res["current"]["temp_c"],
                'icon': res["current"]["condition"]["icon"]
            }
        except KeyError:
            city_info = {
                'city_pk': city.id,
                'city': 'Такого города нет',
                'temp': '-'
            }
        all_cities.append(city_info)
    context = {
        'all_info': all_cities,
        'form': form,
    }
    return render(request, template_name='weather/weather.html', context=context)


def deletecity(request, city_pk):
    city = get_object_or_404(City, pk=city_pk)
    if request.method == 'POST':
        city.delete()
        return redirect('weather')
