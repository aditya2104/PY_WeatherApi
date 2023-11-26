import callAPI
import json
import weather_parser

City = str(input("Enter City Name: "))
statusCode,oridinates = callAPI.coordinates(City)
json_ordinates = json.loads(oridinates)

outList = weather_parser.parse_cities(json_ordinates)
found_cities_num = (len(outList))
if found_cities_num == 1:
    lan = outList[0][1]
    lon = outList[0][2]
    status_code,weather = callAPI.weather(lan,lon)
    print(weather)
elif found_cities_num > 1:
    json_ordinates = json.loads(oridinates)
    dic_cities = weather_parser.select_city(json_ordinates)
    user_dislpay = weather_parser.unpack_dic(**dic_cities)
    
    for line in user_dislpay:
        print(line)
    user_input = input("Please select any one key from above: ")
    while user_input not in dic_cities:
        user_input = input("Wrong key, please select correct key: ")    
    get_city = dic_cities.get(user_input)
    print(get_city)
    Lan,Lon = get_city[1],get_city[2]            
    status_code,weather = callAPI.weather(Lan,Lon)
    print(weather)

else:
    print("Please check city name!")