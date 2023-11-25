import keys
import requests

def coordinates(City):
    geoendpoint = keys.GeoEndPoint+City+"&limit=5&appid="+keys.API
    response = requests.get(geoendpoint)
    statusCode = response.status_code
    response_json = response.text
    return statusCode,response_json
   

def weather(lat,lon):
    weather = keys.WeatherEndpoint+str(lat)+"&lon="+str(lon)+"&appid="+keys.API
    response = requests.get(weather)
    statusCode = requests.status_codes
    response_json = response.text
    return statusCode,response_json



