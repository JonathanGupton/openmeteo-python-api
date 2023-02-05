from enum import Enum

from f1model.weathertools.openmeteoapi.parameters.parameter import URLParameter


class TemperatureUnitValue(Enum):
    Fahrenheit = "fahrenheit"
    Celsius = "celsius"


class TemperatureUnit(URLParameter):
    name = "temperature_unit"
    default = TemperatureUnitValue.Celsius

    def __init__(self, temperature: TemperatureUnitValue):
        if type(temperature) is not TemperatureUnitValue:
            raise TypeError("Must be TemperatureUnitValue type")
        super().__init__(temperature)

    def formatted(self) -> str:
        return self.value.value
