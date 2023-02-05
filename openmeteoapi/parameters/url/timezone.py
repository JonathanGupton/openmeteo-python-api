import zoneinfo

from f1model.weathertools.openmeteoapi.parameters.parameter import URLParameter


TIMEZONES = zoneinfo.available_timezones()


class TimeZone(URLParameter):
    name = "timezone"

    def __init__(self, timezone):
        if timezone not in TIMEZONES:
            raise ValueError("Invalid timezone")
        super().__init__(timezone)

    def formatted(self) -> str:
        return self.value
