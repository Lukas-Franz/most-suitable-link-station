from typing import List

from input_validator import InputValidator

LINK_STATIONS = [
    [0, 0, 10],
    [20, 20, 5],
    [10, 0, 12]
]


def find_most_suitable_link_station(link_stations: List[List[int]]):
    try:
        InputValidator.validate(
            link_stations=link_stations
        )
    except ValueError as e:
        print(f'Input validation failed: {e}')


if __name__ == '__main__':
    find_most_suitable_link_station(
        link_stations=LINK_STATIONS
    )
