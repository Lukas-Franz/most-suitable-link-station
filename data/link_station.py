from dataclasses import dataclass
from typing import List

from data.point import Point


@dataclass
class LinkStation:
    x: int
    y: int
    reach: int

    def position(self) -> Point:
        return Point(self.x, self.y)

    @staticmethod
    def from_list(link_station_as_list: List[int]):
        return LinkStation(
            x=link_station_as_list[0],
            y=link_station_as_list[1],
            reach=link_station_as_list[2]
        )
