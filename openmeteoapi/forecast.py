"""Module containing the Forecast endpoint class"""

from . import __api_version__


class Forecast:
    endpoint = rf"/v{__api_version__}/forecast"

    def __init__(self, openmeteo_obj):
        self._base = openmeteo_obj

    def get(self, parameters):
        return self._base.get(self.endpoint, parameters)
