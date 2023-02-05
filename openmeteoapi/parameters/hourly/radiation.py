"""Module containing the Radiation hourly Parameter"""

from f1model.weathertools.openmeteoapi.parameters.parameter import HourlyParameter


class ShortwaveRadiation(HourlyParameter):
    name = "shortwave_radiation"


class DirectRadiation(HourlyParameter):
    name = "direct_radiation"


class DirectNormalIrradiance(HourlyParameter):
    name = "direct_normal_irradiance"


class DiffuseRadiation(HourlyParameter):
    name = "diffuse_radiation"
