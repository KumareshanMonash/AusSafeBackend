# Define the UserInput model
from pydantic import BaseModel

from .LocationModel import Location


class UserInput(BaseModel):
    skin_tone: str
    skin_type: str
    location_id: int
    activity_level: str
