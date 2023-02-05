"""Module containing the MSL/Surface Pressure Parameters"""

from f1model.weathertools.openmeteoapi.parameters.parameter import HourlyParameter


class MeanSeaLevelPressure(HourlyParameter):
    name = "pressure_msl"


class SurfacePressure(HourlyParameter):
    name = "surface_pressure"
