"""Module containing the Hourly Dew Point Parameter"""

from f1model.weathertools.openmeteoapi.parameters.parameter import HourlyParameter


class DewPoint(HourlyParameter):
    name = "dewpoint_2m"
