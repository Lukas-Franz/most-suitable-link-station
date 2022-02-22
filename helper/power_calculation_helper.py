from typing import List, Optional

from data.link_station import LinkStation
from data.point import Point


class PowerCalculationHelper:
    @staticmethod
    def get_most_suitable_link_station(point: Point, link_stations: List[LinkStation]) -> Optional[LinkStation]:
        most_suitable_link_station: Optional[LinkStation] = None
        greatest_power: float = 0

        for link_station in link_stations:
            power = PowerCalculationHelper.calculate_power(point=point, link_station=link_station)
            if greatest_power < power:
                most_suitable_link_station = link_station
                greatest_power = power

        return most_suitable_link_station

    @staticmethod
    def calculate_power(point: Point, link_station: LinkStation) -> float:
        distance = point.calculate_distance_to_point(link_station.position())
        return pow(link_station.reach - distance, 2) if distance < link_station.reach else 0
