from fastapi import FastAPI, Query, HTTPException, Depends
from typing import List, Optional
import httpx
from sqlalchemy.orm import Session
from . import schemas, crud
from .database import SessionLocal
from .models.SunProtectionModel import SunProtectionRecommendation
from .models.UserInputModel import UserInput

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/locations", response_model=List[schemas.Location])
async def read_locations(
    search_param: Optional[str] = Query(None, min_length=1, max_length=50),
    db: Session = Depends(get_db)
):
    locations = crud.get_locations(db=db, search_param=search_param)
    if not locations:
        raise HTTPException(status_code=404, detail="No locations found matching the search criteria.")
    return locations


# Your Ambee API key
API_KEY = '713292fcfda57c80154b0941b40bdae6bf33c9a38a2390637e883c93a0c9b1a1'


@app.get("/weather")
async def get_weather(location_id: str, db: Session = Depends(get_db)):
    # Retrieve location from the database
    location = crud.get_location_by_id(db, location_id)
    if location is None:
        raise HTTPException(status_code=404, detail="Location not found")

    # Ambee Weather API endpoint
    url = f"https://api.ambeedata.com/weather/latest/by-lat-lng?lat={location.lat}&lng={location.long}"

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
async def get_sun_protection_recommendation(user_input: UserInput, db: Session = Depends(get_db)):
    # Retrieve location details
    location = crud.get_location_by_id(db, user_input.location_id)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")

    # Fetch UV Index from Ambee's Weather API
    url = f"https://api.ambeedata.com/weather/latest/by-lat-lng?lat={location.lat}&lng={location.long}"
    headers = {
        'x-api-key': 'YOUR_API_KEY',
        'Content-type': 'application/json'
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        
    print(response)

    if response.status_code == 200:
        data = response.json()
        print(data)
        uv_index = data.get('data', {}).get('uvIndex')
        if uv_index is None:
            raise HTTPException(status_code=500, detail="UV Index data not available")
    else:
        raise HTTPException(status_code=response.status_code, detail="Error fetching UV Index data")

    # Match user input and UV Index to a recommendation
    # Assuming you have a function or logic to get recommendations based on uv_index, skin_tone, skin_type, and activity_level
    recommendation = get_recommendation(uv_index, user_input.skin_tone, user_input.skin_type, user_input.activity_level)
    if not recommendation:
        raise HTTPException(status_code=404, detail="No suitable sun protection recommendation found")

    return recommendation

@app.get("/")
async def root():
    return {"message": "Welcome to the Locations API!"}
