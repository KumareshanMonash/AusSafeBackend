from pydantic import BaseModel


class SunProtectionRecommendation(BaseModel):
    type_of_clothing: str
    amount_of_sunscreen: str
    type_of_sunscreen: str
    reapply_frequency: str
    max_sun_exposure_time: str
