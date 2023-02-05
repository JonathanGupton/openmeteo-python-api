"""Module containing the WindDirection Parameter"""

from f1model.weathertools.openmeteoapi.parameters.parameter import HourlyParameter


WINDDIRECTION_HEIGHTS = {10, 80, 120, 180}


class WindDirection(HourlyParameter):
    name = "winddirection"

    def __init__(self, height: int):
        if height not in WINDDIRECTION_HEIGHTS:
            raise ValueError(f"Height must be one of {WINDDIRECTION_HEIGHTS}")
        else:
            self.height = height

    def formatted(self) -> str:
        return self.name + "_" + str(self.height) + "m"
