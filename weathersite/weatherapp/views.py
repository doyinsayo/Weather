from django.shortcuts import render
import requests
import pandas as pd
from bs4 import BeautifulSoup
from .models import City


# Create your views here.
def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=a64b1b201212227009268a3a22578166'
    cities = City.objects.all() #return all the cities in the database
    city = 'Lagos'
    city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types 
    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }
    stuff_for_frontend = {'weather' : weather}
    return render(request,'weatherapp/base.html',stuff_for_frontend)

    