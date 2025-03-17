# Define the Location model
from pydantic import BaseModel
from typing import Optional


class Location(BaseModel):
    id: int
    location_name: str
    state: str
    country: str
    zipcode: str
    latitude: float
    longitude: float
    area: Optional[str] = None
