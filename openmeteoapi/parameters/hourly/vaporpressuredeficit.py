"""Module containing the vapor pressure deficit hourly Parameter"""

from f1model.weathertools.openmeteoapi.parameters.parameter import HourlyParameter


class VaporPressureDeficit(HourlyParameter):
    name = "vapor_pressure_deficit"
