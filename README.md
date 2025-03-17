# SunSafeAUS Backend

This repository contains the backend code for the SunSafeAUS application, which provides sun protection recommendations based on user input and current weather data.

## Features

- **Location Management**: Retrieve and manage location data, including postcodes, localities, states, and geographical coordinates.
- **Weather Integration**: Fetch current weather and UV index data using external APIs based on user location.
- **Sun Protection Recommendations**: Provide tailored sun protection advice considering UV index, skin tone, skin type, and activity level.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Models and Schemas](#models-and-schemas)
- [Database Configuration](#database-configuration)
- [Dependencies](#dependencies)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/SunSafeAUS.git
   cd SunSafeAUS/backend
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use 'env\Scripts\activate'
    ```

3. **Install Dependencies:**

   ```bash
    pip install -r requirements.txt
    ```

4. **Run the APplication:**

   ```bash
    uvicorn app.main:app --reload
    ```

## Project STructure
    SunSafeAus/
        ├── app/
        │   ├── __init__.py
        │   ├── main.py
        │   ├── crud.py
        │   ├── database.py
        │   ├── schemas.py
        │   └── models/
        │       ├── __init__.py
        │       ├── SunProtectionModel.py
        │       └── UserInputModel.py
        ├── requirements.txt
        └── README.md

    app/main.py: Contains the FastAPI application and endpoint definitions.
    app/crud.py: Implements the CRUD operations for database interactions.
    app/database.py: Sets up the database connection and ORM configurations.
    app/schemas.py: Defines the Pydantic models for data validation and serialization.
    app/models/: Contains SQLAlchemy models representing database tables.
    requirements.txt: Lists the Python dependencies for the project.
    README.md: Provides an overview and instructions for the project.



## API Endpoints

### Location Endpoints

#### Retrieve Locations

- **Endpoint:** `GET /locations`
- **Query Parameters:**
  - `search_param` (optional): A string to search for matching locations by locality, postcode, or state.
- **Response:** A JSON array of location objects matching the search criteria.

#### Retrieve Weather Data

- **Endpoint:** `GET /weather`
- **Query Parameters:**
  - `location_id` (required): The ID of the location for which to fetch weather data.
- **Response:** A JSON object containing the latest weather data for the specified location.

### Sun Protection Recommendation Endpoint

#### Get Sun Protection Recommendation

- **Endpoint:** `POST /sun_protection`
- **Request Body:** A JSON object with the following structure:
  ```json
  {
    "location": {
      "id": int,
      "postcode": int,
      "locality": str,
      "state": str,
      "long": float,
      "lat": float
    },
    "skin_tone": str,
    "skin_type": str,
    "activity_level": str
  }

## Models and Schemas

The application utilizes SQLAlchemy models to define the database structure and Pydantic schemas for data validation and serialization.

### SQLAlchemy Models

**`UVProtectionRecommendation`**

```python
from sqlalchemy import Column, Integer, Float, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UVProtectionRecommendation(Base):
    __tablename__ = 'uv_protection_recommendations'
    id = Column(Integer, primary_key=True, autoincrement=True)
    uv_index_min = Column(Integer, nullable=False)
    uv_index_max = Column(Integer, nullable=False)
    skin_tone = Column(String(10), nullable=False)
    skin_type = Column(String(15), nullable=False)
    activity_level = Column(String(10), nullable=False)
    type_of_clothing = Column(Text, nullable=False)
    amount_of_sunscreen = Column(Text, nullable=False)
    type_of_sunscreen = Column(Text, nullable=False)
    reapply_frequency = Column(Text, nullable=False)
    max_sun_exposure_time = Column(Text, nullable=False)

Note: This model corresponds to the uv_protection_recommendations table in the database, defining columns and their data types.

## Dependencies

To ensure the application functions correctly, the following Python packages are required:

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.&#8203;:contentReference[oaicite:0]{index=0}
- **httpx**: :contentReference[oaicite:1]{index=1}&#8203;:contentReference[oaicite:2]{index=2}
- **SQLAlchemy**: :contentReference[oaicite:3]{index=3}&#8203;:contentReference[oaicite:4]{index=4}
- **Pydantic**: :contentReference[oaicite:5]{index=5}&#8203;:contentReference[oaicite:6]{index=6}
- **Dash**: :contentReference[oaicite:7]{index=7}&#8203;:contentReference[oaicite:8]{index=8}
- **pandas**: :contentReference[oaicite:9]{index=9}&#8203;:contentReference[oaicite:10]{index=10}
- **plotly**: :contentReference[oaicite:11]{index=11}&#8203;:contentReference[oaicite:12]{index=12}
- **numpy**: :contentReference[oaicite:13]{index=13}&#8203;:contentReference[oaicite:14]{index=14}

:contentReference[oaicite:15]{index=15}&#8203;:contentReference[oaicite:16]{index=16}

## Notes

- **API Key Management**: :contentReference[oaicite:17]{index=17}&#8203;:contentReference[oaicite:18]{index=18}

- **Database Configuration**: :contentReference[oaicite:19]{index=19}&#8203;:contentReference[oaicite:20]{index=20}

- **CORS Middleware**: :contentReference[oaicite:21]{index=21}&#8203;:contentReference[oaicite:22]{index=22}

- **Data Validation**: :contentReference[oaicite:23]{index=23}&#8203;:contentReference[oaicite:24]{index=24}

- **Frontend Integration**: :contentReference[oaicite:25]{index=25}&#8203;:contentReference[oaicite:26]{index=26}

- **Security Considerations**: :contentReference[oaicite:27]{index=27}&#8203;:contentReference[oaicite:28]{index=28}

- **Error Handling**: :contentReference[oaicite:29]{index=29}&#8203;:contentReference[oaicite:30]{index=30}

- **Logging**: :contentReference[oaicite:31]{index=31}&#8203;:contentReference[oaicite:32]{index=32}

:contentReference[oaicite:33]{index=33}&#8203;:contentReference[oaicite:34]{index=34}
