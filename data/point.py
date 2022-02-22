from __future__ import annotations

import math


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def calculate_distance_to_point(self, point: Point) -> float:
        dx = self.x - point.x
        dy = self.y - point.y

        return math.hypot(dx, dy)
