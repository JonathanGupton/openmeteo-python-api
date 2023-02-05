"""Nodule containing the daily weather code parameter"""

from f1model.weathertools.openmeteoapi.parameters.parameter import DailyParameter


class WeatherCode(DailyParameter):
    """The most severe weather condition on a given day"""

    name = "weathercode"
