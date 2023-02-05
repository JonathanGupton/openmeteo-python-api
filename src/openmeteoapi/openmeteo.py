import importlib
from typing import Optional
from typing import Sequence

import requests
import tenacity

from f1model.weathertools.openmeteoapi import __api_version__
from f1model.weathertools.openmeteoapi import __api_base__
from f1model.weathertools.openmeteoapi.parameters.parameter import DailyParameter
from f1model.weathertools.openmeteoapi.parameters.parameter import HourlyParameter
from f1model.weathertools.openmeteoapi.parameters.parameter import URLParameter


class OpenMeteo:
    """Use this class to call the OpenMeteo API"""

    def __init__(self, api_base=__api_base__, api_version=__api_version__):
        self._api_base = api_base
        self._api_version = api_version

    def __getattr__(self, name):
        """
        Handle subclass instantiation.
        Args:
            name (str): Name of open-meteo API to instantiate
        Returns:
             Instance of named class.
        """
        try:
            # api class first
            class_ = getattr(
                importlib.import_module(__package__ + "." + name.lower()), name
            )
            return class_(self)
        except ImportError:
            # model class next:
            try:
                class_ = getattr(importlib.import_module(name.lower()), name)
                return class_()
            except ImportError:
                self._log.error(
                    "ImportError! Could not load api or model class %s", name
                )
                return name

    def make_request_string(
        self,
        endpoint: str,
        url_params: Sequence[URLParameter],
        hourly_params: Optional[Sequence[HourlyParameter]] = None,
        daily_params: Optional[Sequence[DailyParameter]] = None,
    ) -> str:
        url_string = make_url_param_string(url_params)
        hourly_string = make_hourly_param_string(hourly_params)
        daily_string = make_daily_param_string(daily_params)
        url = self._api_base + endpoint + url_string + hourly_string + daily_string
        return url

    def get(
        self,
        endpoint: str,
        url_params: Sequence[URLParameter],
        hourly_params: Optional[Sequence[HourlyParameter]] = None,
        daily_params: Optional[Sequence[DailyParameter]] = None,
    ):
        self.make_request_string(endpoint, url_params, hourly_params, daily_params)

    def request(self, prepped_request):
        """Make a request from the open-meteo API."""
        pass


def make_url_param_string(url_params: Sequence[URLParameter]) -> str:
    """Create the URL Parameter segment for the Open-Meteo API"""
    return "?" + "&".join(
        [param.name + "=" + param.formatted() for param in url_params]
    )


def make_hourly_param_string(hourly_params: Sequence[HourlyParameter]) -> str:
    """Create the Hourly Parameter segment for the Open-Meteo API"""
    if not hourly_params:
        return ""
    return "&hourly=" + ",".join([param.formatted() for param in hourly_params])


def make_daily_param_string(daily_params: Sequence[DailyParameter]) -> str:
    """Create the Daily Parameter segment for the Open-Meteo API"""
    if not daily_params:
        return ""
    return "&daily=" + ",".join([param.formatted() for param in daily_params])
