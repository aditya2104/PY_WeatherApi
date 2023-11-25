import keys
import requests

def coordinates():
    City = str(input("Enter City Name: "))
    geoendpoint = keys.GeoEndPoint+City+"&limit=5&appid="+keys.API
    response = requests.get(geoendpoint)
    statusCode = response.status_code
    response_json = response.text
    return statusCode,response_json
   

def weather():
    pass



