# most-suitable-link-station
Calculates the most suitable link station (based on power) for a given point and a given list of available link stations.

# Usability
You can either use the ```PowerCalculationHelper```, which provides the method ```get_most_suitable_link_station(Point, List[LinkStation])``` to retrieve the LinkStation directly:
```
point = Point(0, 0)
link_stations = [
  LinkStation(0, 0, 10),
  LinkStation(20, 20, 5),
  LinkStation(10, 0, 12)
]

PowerCalculationHelper.get_most_suitable_link_station(
    point=target_point,
    link_stations=link_stations
)
```


Or you can modify the variables in the main.py to make use of the methods provided for output.
