from fastapi import FastAPI, Query, HTTPException
from typing import List, Optional
import httpx

from .dummydata.dummydata import dummy_locations, dummy_recommendations
from .models.LocationModel import Location
from .models.SunProtectionModel import SunProtectionRecommendation
from .models.UserInputModel import UserInput

app = FastAPI()


@app.get("/locations", response_model=List[Location])
async def get_locations(
        searchParam: Optional[str] = Query(None, min_length=1, max_length=50)
):
    if searchParam:
        search_lower = searchParam.lower()
        results = [
            loc for loc in dummy_locations
            if search_lower in loc.location_name.lower()
               or search_lower in loc.zipcode.lower()
               or search_lower in loc.state.lower()
        ]
    else:
        results = dummy_locations
    return results


# Your Ambee API key
API_KEY = '713292fcfda57c80154b0941b40bdae6bf33c9a38a2390637e883c93a0c9b1a1'


@app.get("/weather")
async def get_weather(location_name: str):
    # Simulate database lookup
    location = next((loc for loc in dummy_locations if loc.location_name.lower() == location_name.lower()), None)
    if location is None:
        raise HTTPException(status_code=404, detail="Location not found")

    # Ambee Weather API endpoint
    url = f"https://api.ambeedata.com/weather/latest/by-lat-lng?lat={location.latitude}&lng={location.longitude}"

    headers = {
        'x-api-key': API_KEY,
        'Content-type': 'application/json'
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)

    if response.status_code == 200:
        # Parse the JSON response and return relevant data
        data = response.json()
        return data
    else:
        raise HTTPException(status_code=response.status_code, detail="Error fetching weather data")


@app.post("/sun_protection", response_model=SunProtectionRecommendation)
async def get_sun_protection_recommendation(user_input: UserInput):
    # Fetch UV Index from Ambee's Weather API
    url = f"https://api.ambeedata.com/weather/latest/by-lat-lng?lat={user_input.location.latitude}&lng={user_input.location.longitude}"
    headers = {
        'x-api-key': API_KEY,
        'Content-type': 'application/json'
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        uv_index = data.get('data', {}).get('uvIndex', None)
        if uv_index is None:
            raise HTTPException(status_code=500, detail="UV Index data not available")
    else:
        raise HTTPException(status_code=response.status_code, detail="Error fetching UV Index data")

    # Match user input and UV Index to a recommendation
    for recommendation in dummy_recommendations:
        uv_min, uv_max = recommendation["uv_index_range"]
        if (uv_min <= uv_index <= uv_max and
                recommendation["skin_tone"] == user_input.skin_tone.lower() and
                recommendation["skin_type"] == user_input.skin_type.lower() and
                recommendation["activity_level"] == user_input.activity_level.lower()):
            return recommendation["recommendation"]

    # Default recommendation if no match is found
    raise HTTPException(status_code=404, detail="No suitable sun protection recommendation found")


@app.get("/")
async def root():
    return {"message": "Welcome to the Locations API!"}
