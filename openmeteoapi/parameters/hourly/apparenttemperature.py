"""Module containing the Apparent Temperature Parameter"""

from f1model.weathertools.openmeteoapi.parameters.parameter import HourlyParameter


class ApparentTemperature(HourlyParameter):
    name = "apparent_temperature"
