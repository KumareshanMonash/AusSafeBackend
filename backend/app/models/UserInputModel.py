# Define the UserInput model
from pydantic import BaseModel

from ..schemas import Location


class UserInput(BaseModel):
    skin_tone: str
    skin_type: str
    location: Location
    activity_level: str
