from sqlalchemy import text
from sqlalchemy.orm import Session
from app.api.categories.models import Category
from app.api.locations.models import Location
from app.api.recommendations.models import LocationCategoryReview
from app.api.recommendations.schemas import LocationCategoryReviewCreate

def get_unreviewed_location_categories(db: Session):
    locations = db.query(LocationCategoryReview, Category, Location).join(Category)\
        .join(Location).filter(LocationCategoryReview.last_reviewed.is_(None))\
        .limit(10)\
            .all()
    
    if len(locations) < 10:
        locations_reviwed = db.query(LocationCategoryReview, Category, Location).join(Category)\
        .join(Location)\
              .filter(LocationCategoryReview.last_reviewed <= text('CURRENT_DATE - INTERVAL \'30 days\''))\
              .order_by(LocationCategoryReview.last_reviewed)\
              .limit(10-len(locations))\
              .all()
        locations += locations_reviwed

    locations_json = []

    for location_review, category, location in locations:
        location_dict = {
            "location_category_review_id": location_review.id,
            "last_reviewed": location_review.last_reviewed,
            "category_id": category.id,
            "category_name": category.name,
            "location_id": location.id,
            "location_longitude": location.longitude,
            "location_latitude": location.latitude,
        }
        locations_json.append(location_dict)
    return locations_json


def create_location_category_reviews(db: Session, location_category_review: LocationCategoryReviewCreate):
    db_location_category_review = LocationCategoryReview(**location_category_review.model_dump())
    db.add(db_location_category_review)
    db.commit()
    db.refresh(db_location_category_review)
    return db_location_category_review
