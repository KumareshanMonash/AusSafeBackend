# app/crud.py
from typing import Optional, List
from sqlalchemy.orm import Session
from . import model
from sqlalchemy import func, or_, cast, String, and_

from .schemas import SunProtectionRecommendation


def get_locations(db: Session, search_param: Optional[str] = None, limit: int = 100) -> List[model.Location]:
    query = db.query(
        model.Location.id,
        model.Location.postcode,
        model.Location.locality,
        model.Location.state,
        model.Location.long,
        model.Location.lat
    )
    if search_param:
        search_pattern = f"%{search_param.lower()}%"
        query = query.filter(
            or_(
                func.lower(model.Location.locality).ilike(search_pattern),
                func.lower(cast(model.Location.postcode, String)).ilike(search_pattern),
                func.lower(model.Location.state).ilike(search_pattern)
            )
        )
    return query.limit(limit).all()


def get_location_by_id(db: Session, location_id: str):
    return db.query(model.Location).filter(model.Location.id == location_id).first()

def get_recommendation(db: Session, uv_index: int, skin_tone: str, skin_type: str, activity_level: str) -> Optional[SunProtectionRecommendation]:
    result = db.query(
        model.UVProtectionRecommendation.type_of_clothing,
        model.UVProtectionRecommendation.amount_of_sunscreen,
        model.UVProtectionRecommendation.type_of_sunscreen,
        cast(model.UVProtectionRecommendation.reapply_frequency, Integer),
        model.UVProtectionRecommendation.max_sun_exposure_time
    ).filter(
        and_(
            model.UVProtectionRecommendation.uv_index_min <= uv_index,
            model.UVProtectionRecommendation.uv_index_max >= uv_index,
            model.UVProtectionRecommendation.skin_tone == skin_tone.lower(),
            model.UVProtectionRecommendation.skin_type == skin_type.lower(),
            model.UVProtectionRecommendation.activity_level == activity_level.lower()
        )
    ).first()
    print("result",result)
    if result:
        return SunProtectionRecommendation(
            type_of_clothing=result.type_of_clothing,
            amount_of_sunscreen=result.amount_of_sunscreen,
            type_of_sunscreen=result.type_of_sunscreen,
            reapply_frequency=int(result.reapply_frequency),
            max_sun_exposure_time=result.max_sun_exposure_time
        )
    return None
