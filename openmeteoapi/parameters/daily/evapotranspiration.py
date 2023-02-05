"""Nodule containing daily evapotranspiration parameters"""

from f1model.weathertools.openmeteoapi.parameters.parameter import DailyParameter


class ET0FAOEvapotranspiration(DailyParameter):
    """Daily sum of ET₀ Reference Evapotranspiration of a well watered grass field"""

    name = "et0_fao_evapotranspiration"
