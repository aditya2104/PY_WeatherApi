import callAPI
import json
import weather_parser

City = str(input("Enter City Name: "))
statusCode,oridinates = callAPI.coordinates(City)
json_ordinates = json.loads(oridinates)
outList = weather_parser.parse_cities(json_ordinates)
found_cities_num = (len(outList))
# print((outList))
if found_cities_num == 1:
    #call func weather
    lan = outList[0][1]
    lon = outList[0][2]
    # print(lan,lon)
    status_code,weather = callAPI.weather(lan,lon)
    print(weather)
    #call func parse_weather
elif found_cities_num > 1:
    pass
    #user input 
    #call func weather