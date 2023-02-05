"""Module containing the Cape hourly Parameter"""

from f1model.weathertools.openmeteoapi.parameters.parameter import HourlyParameter


class Cape(HourlyParameter):
    """Convective available potential energy"""

    name = "cape"
