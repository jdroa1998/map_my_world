from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.api.recommendations.schemas import LocationCategoryReview
from app.api.recommendations.schemas import LocationCategoryReviewCreate
from app.api.recommendations.services import create_location_category_reviews, get_unreviewed_location_categories

from ...core.database import get_db

router = APIRouter()

@router.get("/")
def get_recommendations(db: Session = Depends(get_db)):
    return get_unreviewed_location_categories(db=db)

@router.post("/", response_model=LocationCategoryReview)
def create_location_category_reviews_endpoint(location_category_review: LocationCategoryReviewCreate, db: Session = Depends(get_db)):
    return create_location_category_reviews(db=db, location_category_review=location_category_review)
