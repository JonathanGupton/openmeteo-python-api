"""Module containing the Archive endpoint class"""
from typing import Optional
from typing import Sequence

from . import __api_version__

from f1model.weathertools.openmeteoapi.parameters.parameter import DailyParameter
from f1model.weathertools.openmeteoapi.parameters.parameter import HourlyParameter
from f1model.weathertools.openmeteoapi.parameters.parameter import URLParameter


class Archive:
    endpoint = rf"/v{__api_version__}/archive"

    def __init__(self, openmeteo_obj):
        self._base = openmeteo_obj

    def get(
        self,
        url_params: Sequence[URLParameter],
        hourly_params: Optional[Sequence[HourlyParameter]] = None,
        daily_params: Optional[Sequence[DailyParameter]] = None,
    ):
        return self._base.get(self.endpoint, url_params, hourly_params, daily_params)
