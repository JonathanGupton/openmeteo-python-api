"""Module containing the Hourly Relative Humidity Parameter"""

from f1model.weathertools.openmeteoapi.parameters.parameter import HourlyParameter


class RelativeHumidity(HourlyParameter):
    name = "relativehumidity_2m"
