from django.shortcuts import render
import requests
import pandas as pd
from bs4 import BeautifulSoup
from .models import City
from .forms import CityForm


# Create your views here.
def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=a64b1b201212227009268a3a22578166'
   
    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate

    cities = City.objects.all() #return all the cities in the database
    form = CityForm()
    weather_data = []
    for city in cities:
        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types 
       
        weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
        }
        weather_data.append(weather)
        #adding the contents of the weather dict to the empty list: weather_data

    stuff_for_frontend = {'weather_data' : weather_data ,'form' : form}
    return render(request,'weatherapp/base.html',stuff_for_frontend)

    