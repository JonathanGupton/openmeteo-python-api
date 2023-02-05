"""Module containing the Precipitation hourly Parameter"""

from f1model.weathertools.openmeteoapi.parameters.parameter import HourlyParameter


class Precipitation(HourlyParameter):
    name = "precipitation"
