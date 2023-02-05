"""Module containing the Evapotranspiration Parameters"""

from f1model.weathertools.openmeteoapi.parameters.parameter import HourlyParameter


class Evapotranspiration(HourlyParameter):
    """
    Evapotranspration from land surface and plants that weather models assumes
    for this location. Available soil water is considered. 1 mm
    evapotranspiration per hour equals 1 liter of water per spare meter.
    """

    name = "evapotranspiration"


class ET0FAOEvapotranspiration(HourlyParameter):
    """
    ET₀ Reference Evapotranspiration of a well watered grass field. Based on
    FAO-56 Penman-Monteith equations ET₀ is calculated from temperature, wind
    speed, humidity and solar radiation. Unlimited soil water is assumed. ET₀
    is commonly used to estimate the required irrigation for plants.
    """

    name = "et0_fao_evapotranspiration"
