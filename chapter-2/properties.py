class Coordinates:
    def __init__(self, latitude: float, longitude: float) -> None:
        self.latitude = latitude
        self.longitude = longitude

    @property
    def latitude(self) -> None:
        return self.latitude
    
    @latitude.setter
    def latitude(self, latitude_value:float) ->None:
        if latitude_value not in range(-90, 90):
            raise ValueError(
                f"{latitude_value} is an invalid value for latitude")
        
    @property
    def longitude(self) -> None:
        return self.longitude
    
    @longitude.setter
    def longitude(self, long_val: float) -> None:
        if long_val not in range(-180, 180):
            raise ValueError(
                f"{long_val} is an invalid value for longitude"
            )



