"""Module containing the Weather Code hourly Parameter"""

from f1model.weathertools.openmeteoapi.parameters.parameter import HourlyParameter


class WeatherCode(HourlyParameter):
    """Weather condition as a numeric code. Follow WMO weather interpretation codes. See table below for details."""

    name = "weathercode"
