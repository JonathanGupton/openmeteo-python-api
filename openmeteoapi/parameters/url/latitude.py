from f1model.weathertools.openmeteoapi.parameters.parameter import URLParameter


class Latitude(URLParameter):
    """Class representing the Latitude URL Parameter"""

    name = "latitude"
    description = "Geographical WGS84 latitude of the location"

    def __init__(self, latitude: float):
        if type(latitude) is not float:
            raise ValueError("Latitude most be float")
        super().__init__(latitude)

    def formatted(self):
        return str(self.value)
