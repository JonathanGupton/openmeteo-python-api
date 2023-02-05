"""Module containing the Past Days URL Parameters"""

from f1model.weathertools.openmeteoapi.parameters.parameter import URLParameter


MIN_PAST_DAYS = 0
MAX_PAST_DAYS = 2


class PastDays(URLParameter):
    name = "past_days"
    default = 0

    def __init__(self, days: int):
        if days < MIN_PAST_DAYS or days > MAX_PAST_DAYS:
            raise ValueError(
                f"PastDays can only accept values between {MIN_PAST_DAYS} and {MAX_PAST_DAYS} inclusive"
            )
        super().__init__(days)

    def formatted(self) -> str:
        return str(self.value)
