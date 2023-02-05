"""Module containing the showers hourly Parameter"""

from f1model.weathertools.openmeteoapi.parameters.parameter import HourlyParameter


class Showers(HourlyParameter):
    """Showers from convective precipitation in millimeters from the preceding hour"""

    name = "showers"
