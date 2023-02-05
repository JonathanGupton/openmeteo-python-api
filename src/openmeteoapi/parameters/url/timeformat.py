from enum import Enum

from f1model.weathertools.openmeteoapi.parameters.parameter import URLParameter


class TimeFormatValue(Enum):
    ISO8601 = "iso8601"
    UnixTime = "unixtime"


class TimeFormat(URLParameter):
    name = "timeformat"
    default = TimeFormatValue.ISO8601

    def __init__(self, time_format: TimeFormatValue):
        super().__init__(time_format)

    def formatted(self) -> str:
        return self.value.value
