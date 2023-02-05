"""Nodule containing daily wind parameters"""

from f1model.weathertools.openmeteoapi.parameters.parameter import DailyParameter


class WindSpeedMax(DailyParameter):
    """Maximum wind speed on a day"""

    name = "windspeed_10m_max"


class WindGustMax(DailyParameter):
    """Maximum wind gusts on a day"""

    name = "windgusts_10m_max"


class DominantWindDirection(DailyParameter):
    """Dominant wind direction"""

    name = "winddirection_10m_dominant"
