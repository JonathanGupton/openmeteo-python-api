"""Module containing the Wind Gusts Parameter"""

from f1model.weathertools.openmeteoapi.parameters.parameter import HourlyParameter


class WindGusts(HourlyParameter):
    name = "windgusts_10m"
