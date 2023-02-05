from enum import Enum

from f1model.weathertools.openmeteoapi.parameters.parameter import URLParameter


class WindSpeedUnitValue(Enum):
    KilometersPerHour = "kmh"
    Knots = "kn"
    MilesPerHour = "mph"
    MetersPerSecond = "ms"


class WindSpeedUnit(URLParameter):
    name = "windspeed_unit"
    default = WindSpeedUnitValue.KilometersPerHour

    def __init__(self, windspeed_unit: WindSpeedUnitValue):
        if type(windspeed_unit) is not WindSpeedUnitValue:
            raise TypeError("Must be WindSpeedUnitValue type")
        super().__init__(windspeed_unit)

    def formatted(self) -> str:
        return self.value.value
