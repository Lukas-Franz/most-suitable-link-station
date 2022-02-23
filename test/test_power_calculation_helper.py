import unittest

from data.link_station import LinkStation
from data.point import Point
from helper.power_calculation_helper import PowerCalculationHelper

POINT_A = Point(0, 0)
LINK_STATION_A = LinkStation(0, 0, 10)

POINT_B = Point(20, 15)
LINK_STATION_B = LinkStation(5, 7, 3)

POINT_C = Point(13, 11)
LINK_STATION_C = LinkStation(9, 1, 20)

POINT_D = Point(-8, 4)
LINK_STATION_D = LinkStation(23, -5, 25)

POINT_E = Point(-1, 9)
LINK_STATION_E = LinkStation(2, 3, 16)

VALID_POWER_A_TO_A: float = 100
VALID_POWER_A_TO_B: float = 0  # out of reach
VALID_POWER_B_TO_D: float = 22.812579192165778
VALID_POWER_C_TO_D: float = 37.601886794339634
VALID_POWER_C_TO_E: float = 5.75294372046581
INVALID_POWER_C_TO_D: float = 50


class TestPowerCalculationHelper(unittest.TestCase):
    def test_with_valid_power_point_a_to_a(self):
        power = PowerCalculationHelper.calculate_power(POINT_A, LINK_STATION_A)
        self.assertTrue(power == VALID_POWER_A_TO_A)

    def test_with_valid_power_point_a_to_b(self):
        power = PowerCalculationHelper.calculate_power(POINT_A, LINK_STATION_B)
        self.assertTrue(power == VALID_POWER_A_TO_B)

    def test_with_valid_power_point_b_to_d(self):
        power = PowerCalculationHelper.calculate_power(POINT_B, LINK_STATION_D)
        self.assertTrue(power == VALID_POWER_B_TO_D)

    def test_with_valid_power_point_c_to_d(self):
        power = PowerCalculationHelper.calculate_power(POINT_C, LINK_STATION_D)
        self.assertTrue(power == VALID_POWER_C_TO_D)

    def test_with_valid_power_point_c_to_e(self):
        power = PowerCalculationHelper.calculate_power(POINT_C, LINK_STATION_E)
        self.assertTrue(power == VALID_POWER_C_TO_E)

    def test_with_invalid_power_point_c_to_d(self):
        power = PowerCalculationHelper.calculate_power(POINT_C, LINK_STATION_D)
        self.assertFalse(power == INVALID_POWER_C_TO_D)
