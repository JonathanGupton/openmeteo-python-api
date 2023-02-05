"""Module containing the Hourly Temperature Parameter"""

from f1model.weathertools.openmeteoapi.parameters.parameter import HourlyParameter


class Temperature(HourlyParameter):
    name = "temperature_2m"
