"""Nodule containing daily temperature parameters"""

from f1model.weathertools.openmeteoapi.parameters.parameter import DailyParameter


class TemperatureMax(DailyParameter):
    """Maximum daily air temperature at 2 meters above ground"""

    name = "temperature_2m_max"


class TemperatureMin(DailyParameter):
    """Minimum daily air temperature at 2 meters above ground"""

    name = "temperature_2m_min"


class ApparentTemperatureMax(DailyParameter):
    """Maximum daily apparent temperature"""

    name = "apparent_temperature_max"


class ApparentTemperatureMin(DailyParameter):
    """Minimum daily apparent temperature"""

    name = "apparent_temperature_min"
