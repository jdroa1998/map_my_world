from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.locations.schemas import Location
from app.api.locations.schemas import LocationCreate
from app.api.locations.services import create_location
from ...core.database import get_db

router = APIRouter()

@router.post("/", response_model=Location)
def create_location_endpoint(location: LocationCreate, db: Session = Depends(get_db)):
    return create_location(db=db, location=location)
