from typing import List


class InputValidator:
    @staticmethod
    def validate(link_stations: List[List[int]]) -> bool:
        flattened_entries = [entry for station in link_stations for entry in station]

        if any(type(entry) != int for entry in flattened_entries) or any(entry < 0 for entry in flattened_entries):
            raise ValueError('Only whole numbers are allowed.')

        return True
