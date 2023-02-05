"""Module containing the Soil Temperature hourly Parameter"""

from f1model.weathertools.openmeteoapi.parameters.parameter import HourlyParameter


SOIL_TEMPERATURE_DEPTHS = {0, 6, 18, 54}


class SoilTemperature(HourlyParameter):
    """Temperature in the soil at 0, 6, 18 and 54 cm depths. 0 cm is the
    surface temperature on land or water surface temperature on water.
    """

    name = "soil_temperature"

    def __init__(self, depth: int):
        if depth not in SOIL_TEMPERATURE_DEPTHS:
            raise ValueError(
                f"{depth} not in allowed depths: {SOIL_TEMPERATURE_DEPTHS}"
            )
        self.depth = depth

    def formatted(self) -> str:
        return self.name + "_" + str(self.depth) + "cm"
