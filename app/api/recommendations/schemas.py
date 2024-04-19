from pydantic import BaseModel
from typing import Optional
import datetime

class LocationCategoryReviewCreate(BaseModel):
    location_id: int
    category_id: int
    last_reviewed:  Optional[datetime.datetime] = None

class LocationCategoryReview(BaseModel):
    location_id: int
    category_id: int
    last_reviewed:  Optional[datetime.datetime] = None
    id: int
