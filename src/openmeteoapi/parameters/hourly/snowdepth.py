"""Module containing the Snowdepth hourly Parameter"""

from f1model.weathertools.openmeteoapi.parameters.parameter import HourlyParameter


class SnowDepth(HourlyParameter):
    name = "snow_depth"
