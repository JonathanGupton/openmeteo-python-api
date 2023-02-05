from f1model.weathertools.openmeteoapi.parameters.parameter import URLParameter


class Longitude(URLParameter):
    """Class representing the Longitude URL Parameter"""

    name = "longitude"
    description = "Geographical WGS84 longitude of the location"

    def __init__(self, longitude: float):
        if type(longitude) is not float:
            raise ValueError("Longitude most be float")
        super().__init__(longitude)

    def formatted(self):
        return str(self.value)
