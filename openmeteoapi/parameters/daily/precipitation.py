"""Nodule containing daily precipitation parameters"""

from f1model.weathertools.openmeteoapi.parameters.parameter import DailyParameter


class PrecipitationSum(DailyParameter):
    """Sum of daily precipitation (including rain, showers and snowfall)"""

    name = "precipitation_sum"


class RainSum(DailyParameter):
    """Sum of daily rain"""

    name = "rain_sum"


class ShowersSum(DailyParameter):
    """Sum of daily showers"""

    name = "showers_sum"


class SnowfallSum(DailyParameter):
    """Snowfall sum"""

    name = "snowfall_sum"


class PrecipitationHours(DailyParameter):
    """The number of hours with rain"""

    name = "precipitation_hours"
