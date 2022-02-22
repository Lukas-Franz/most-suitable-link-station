import math
import unittest

from data.point import Point

POINT_A = Point(0, 0)
POINT_B = Point(5, 8)

POINT_C = Point(10, 7)
POINT_D = Point(3, 2)

POINT_E = Point(-5, 7)

VALID_DISTANCE_A_TO_B: float = math.sqrt(89)
VALID_DISTANCE_A_TO_C: float = math.sqrt(149)
VALID_DISTANCE_B_TO_D: float = 2 * math.sqrt(10)
VALID_DISTANCE_C_TO_E: float = 15
INVALID_DISTANCE: float = 5


class TestPoint(unittest.TestCase):
    def test_with_valid_distance_point_a_to_b(self):
        distance = POINT_A.calculate_distance_to_point(POINT_B)
        self.assertTrue(distance == VALID_DISTANCE_A_TO_B)

    def test_with_valid_distance_point_a_to_c(self):
        distance = POINT_A.calculate_distance_to_point(POINT_C)
        self.assertTrue(distance == VALID_DISTANCE_A_TO_C)

    def test_with_valid_distance_point_b_to_d(self):
        distance = POINT_B.calculate_distance_to_point(POINT_D)
        self.assertTrue(distance == VALID_DISTANCE_B_TO_D)

    def test_with_valid_distance_point_c_to_e(self):
        distance = POINT_C.calculate_distance_to_point(POINT_E)
        self.assertTrue(distance == VALID_DISTANCE_C_TO_E)

    def test_with_invalid_distance(self):
        distance = POINT_A.calculate_distance_to_point(POINT_B)
        self.assertFalse(distance == INVALID_DISTANCE)
