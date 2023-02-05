from enum import Enum

from f1model.weathertools.openmeteoapi.parameters.parameter import URLParameter


class PrecipitationUnitValue(Enum):
    Millimeter = "mm"
    Inch = "inch"


class PrecipitationUnit(URLParameter):
    name = "precipitation_unit"
    default = PrecipitationUnitValue.Millimeter

    def __init__(self, precipitation_unit: PrecipitationUnitValue):
        if type(precipitation_unit) is not PrecipitationUnitValue:
            raise TypeError("Must be PrecipitationUnitValue type")
        super().__init__(precipitation_unit)

    def formatted(self) -> str:
        return self.value.value
