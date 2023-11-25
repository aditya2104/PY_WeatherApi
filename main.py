import callAPI
import json
import LatLonSelect

statusCode,oridinates = callAPI.coordinates()
json_ordinates = json.loads(oridinates)
outList = []
for i in range(len(json_ordinates)):
    innerList = []
    City = json_ordinates[i]["name"]
    Lat = json_ordinates[i]["lat"]
    Lon = json_ordinates[i]["lon"]
    Country = json_ordinates[i]["country"]
    State = json_ordinates[i]["state"]
    innerList.append(City)
    innerList.append(Lat)
    innerList.append(Lon)
    innerList.append(Country)
    innerList.append(State)
    outList.append(innerList)

print(outList)
# user_Input = LatLonSelect.lat_lon(outList)








