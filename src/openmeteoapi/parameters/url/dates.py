"""Module containing the Start Date and End Date URL Parameters"""

from datetime import datetime

from f1model.weathertools.openmeteoapi.parameters.parameter import URLParameter


DATE_FORMAT = "%Y-%m-%d"


class StartDate(URLParameter):
    name = "start_date"

    def formatted(self) -> str:
        return self.value.strftime(DATE_FORMAT)


class EndDate(URLParameter):
    name = "end_date"

    def __init__(self, date: datetime):
        super().__init__(date)

    def formatted(self) -> str:
        return self.value.strftime(DATE_FORMAT)
