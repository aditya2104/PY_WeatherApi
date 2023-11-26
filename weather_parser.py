def parse_cities(cities):
    outerList = []
    for i in range(len(cities)):
        innerList = []
        City = cities[i]["name"]
        Lat = cities[i]["lat"]
        Lon = cities[i]["lon"]
        Country = cities[i]["country"]
        State = cities[i]["state"]
        innerList.append(City)
        innerList.append(Lat)
        innerList.append(Lon)
        innerList.append(Country)
        innerList.append(State)
        outerList.append(innerList)
    return outerList

def select_city(cities):
    dic_cities = {}
    for i in range(len(cities)):
        City = cities[i]["name"]
        Lat = cities[i]["lat"]
        Lon = cities[i]["lon"]
        Country = cities[i]["country"]
        State = cities[i]["state"]
        dic_cities["Key"+str(i)] = [City,Lat,Lon,Country,State]
    return dic_cities

def unpack_dic(**kwargs):
    for k,v in kwargs.items():
        yield (k+ " - "+ ", ".join(map(str,v)))
