"""Module containing the Soil Moisture hourly Parameter"""
from __future__ import annotations

from f1model.weathertools.openmeteoapi.parameters.parameter import HourlyParameter


SOIL_MOISTURE_DEPTHS = [(0, 1), (1, 3), (3, 9), (9, 27), (27, 81)]


class SoilMoisture(HourlyParameter):
    """
    Average soil water content as volumetric mixing ratio at 0-1, 1-3, 3-9,
    9-27 and 27-81 cm depths.
    """

    name = "soil_moisture"

    def __init__(self, depth: tuple[int, int]):
        if depth not in SOIL_MOISTURE_DEPTHS:
            raise ValueError(
                f"Invalid {depth}, value must be in {SOIL_MOISTURE_DEPTHS}"
            )
        self.depth = depth

    def formatted(self) -> str:
        return self.name + "_" + str(self.depth[0]) + "_" + str(self.depth[1]) + "cm"

    @classmethod
    def from_range(cls, min_depth: int, max_depth: int) -> tuple[SoilMoisture]:
        # TODO:  Implement this
        pass
