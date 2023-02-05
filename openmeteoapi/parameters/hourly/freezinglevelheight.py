"""Module containing the freezing level height hourly Parameter"""

from f1model.weathertools.openmeteoapi.parameters.parameter import HourlyParameter


class FreezingLevelHeight(HourlyParameter):
    """Altitude above sea level of the 0°C level"""

    name = "freezinglevel_height"
