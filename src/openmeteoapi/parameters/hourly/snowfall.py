"""Module containing the Snowfall hourly Parameter"""

from f1model.weathertools.openmeteoapi.parameters.parameter import HourlyParameter


class Snowfall(HourlyParameter):
    name = "snowfall"
