def lat_lon(cities):
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
    print(outerList.append(innerList))