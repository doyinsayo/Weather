from django.shortcuts import render
import requests
import pandas as pd
from bs4 import BeautifulSoup


# Create your views here.
def home(request):
    url = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=a64b1b201212227009268a3a22578166'
    city = 'Lagos'
    city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types 
    return render(request,'weatherapp/base.html')