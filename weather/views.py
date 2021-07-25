import weather
from django.shortcuts import render
import requests
from pprint import pprint
from .forms import CityForm
# Create your views here.

def Home(request):
    url     = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'
    
    city    = None
    form    = CityForm()
    if request.method == 'POST':
        city = request.POST.get('name')
        
    res     = requests.get(url.format(city)).json()
    celsius = int((res['main']['temp']- 32.0) * 5.0/9.0)
    
    context = {
        "city" : city,
        "temperature" : celsius,
        "description" : res['weather'][0]['description'],
        "icon" : res['weather'][0]['icon'],
        'form' : form,
    }
    return render(request,'weather/weather.html',context)