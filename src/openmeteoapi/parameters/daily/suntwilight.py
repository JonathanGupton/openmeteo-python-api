"""Nodule containing daily sunrise and sunset parameter"""

from f1model.weathertools.openmeteoapi.parameters.parameter import DailyParameter


class Sunrise(DailyParameter):
    """Sunrise time"""

    name = "sunrise"


class Sunset(DailyParameter):
    """Sunset time"""

    name = "sunset"
