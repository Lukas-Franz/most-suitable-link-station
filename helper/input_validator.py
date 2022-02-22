from typing import List


class InputValidator:
    @staticmethod
    def validate(link_stations_input: List[List[int]]) -> bool:
        for station in link_stations_input:
            if len(station) != 3:
                raise ValueError('Incorrect number of entries in list. Provide three entries (x, y, reach).')

            for entry in station:
                if type(entry) != int:
                    raise TypeError('Only integers are allowed.')

        return True
