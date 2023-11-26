# PY_WeatherApi

Real time weather condions are returned. 
Calls OpenWeather API to get real time weather conditions of a city. 

User Input - City Name
If multiple cities with same name 
User Input 2 - Select City within a Country and State 

keys.py file needs to be added to the folder with below structure. Add your own API key as indicated below. 

## keys.py file structure 

API = "ADD YOUR API KEY HERE"

GeoEndPoint = "http://api.openweathermap.org/geo/1.0/direct?q="

WeatherEndpoint = "https://api.openweathermap.org/data/2.5/weather?lat="

## Future Plan 
1. Create desktop interface with Tkinter (hopefully pack it as an app )
2. Create web interface with flask/django 