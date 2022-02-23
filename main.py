from typing import List, Optional

from data.link_station import LinkStation
from data.point import Point
from helper.input_validator import InputValidator
from helper.power_calculation_helper import PowerCalculationHelper


def find_most_suitable_link_station(target_point: Point, link_stations_raw: List[List[int]]) -> Optional[LinkStation]:
    try:
        InputValidator.validate(
            link_stations_input=link_stations_raw
        )

        link_stations = [LinkStation.from_list(station) for station in link_stations_raw]

        return PowerCalculationHelper.get_most_suitable_link_station(
            point=target_point,
            link_stations=link_stations
        )
    except ValueError as e:
        print(f'Input validation failed: {e}')
        return None


def print_most_suitable_link_station(target_point: Point, link_stations_raw: List[List[int]]):
    link_station = find_most_suitable_link_station(
        target_point=target_point,
        link_stations_raw=link_stations_raw
    )

    if link_station is None:
        print(f'No link station within reach for point {target_point.x},{target_point.y}')
    else:
        print(
            f'Best link station for point '
            f'{target_point.x},{target_point.y} is '
            f'{link_station.x},{link_station.y} with power '
            f'{PowerCalculationHelper.calculate_power(point=target_point, link_station=link_station)}'
        )


if __name__ == '__main__':
    link_stations_input = [
        [0, 0, 10],
        [20, 20, 5],
        [10, 0, 12]
    ]
    print_most_suitable_link_station(
        target_point=Point(0, 0),
        link_stations_raw=link_stations_input
    )
    print_most_suitable_link_station(
        target_point=Point(100, 100),
        link_stations_raw=link_stations_input
    )
    print_most_suitable_link_station(
        target_point=Point(15, 10),
        link_stations_raw=link_stations_input
    )
    print_most_suitable_link_station(
        target_point=Point(18, 18),
        link_stations_raw=link_stations_input
    )
