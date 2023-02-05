"""Nodule containing daily radiation parameters"""

from f1model.weathertools.openmeteoapi.parameters.parameter import DailyParameter


class ShortwaveRadiationSum(DailyParameter):
    """The sum of solar radiation on a given day in Megajoules"""

    name = "shortwave_radiation_sum"
