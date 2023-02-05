"""Module containing the rain hourly Parameter"""

from f1model.weathertools.openmeteoapi.parameters.parameter import HourlyParameter


class Rain(HourlyParameter):
    """Rain from large scale weather systems of the preceding hour in millimeter"""

    name = "rain"
