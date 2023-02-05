"""Module containing the Cloud Cover Parameter"""

from enum import Enum

from f1model.weathertools.openmeteoapi.parameters.parameter import HourlyParameter


class CloudCoverLevel(Enum):
    Default = ""
    Low = "low"
    Mid = "mid"
    High = "high"


class CloudCover(HourlyParameter):
    name = "cloudcover"

    def __init__(self, level: CloudCoverLevel = CloudCoverLevel.Default):
        self.level = level

    def formatted(self):
        if self.level.value == CloudCoverLevel.Default.value:
            return self.name
        else:
            return self.name + "_" + self.level.value
