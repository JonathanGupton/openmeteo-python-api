"""Module containing the WindSpeed Parameter"""

from f1model.weathertools.openmeteoapi.parameters.parameter import HourlyParameter


WINDSPEED_HEIGHTS = {10, 80, 120, 180}


class WindSpeed(HourlyParameter):
    name = "windspeed"

    def __init__(self, height: int):
        if height not in WINDSPEED_HEIGHTS:
            raise ValueError(f"Speed must be one of {WINDSPEED_HEIGHTS}")
        else:
            self.height = height

    def formatted(self) -> str:
        return self.name + "_" + str(self.height) + "m"
