from pydantic import BaseModel

class LocationCreate(BaseModel):
    longitude: float
    latitude: float

class Location(BaseModel):
    longitude: float
    latitude: float
    id: int