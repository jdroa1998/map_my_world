from sqlalchemy.orm import Session
from app.api.locations.models import Location
from app.api.locations.schemas import LocationCreate

def create_location(db: Session, location: LocationCreate):
    db_location = Location(**location.model_dump())
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location
