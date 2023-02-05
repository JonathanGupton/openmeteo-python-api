"""Module containing the visibility hourly Parameter"""

from f1model.weathertools.openmeteoapi.parameters.parameter import HourlyParameter


class Visibility(HourlyParameter):
    """Viewing distance in meters. Influenced by low clouds, humidity and
    aerosols. Maximum visibility is approximately 24 km."""

    name = "visibility"
