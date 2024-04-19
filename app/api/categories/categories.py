from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.categories.schemas import Category
from app.api.categories.schemas import CategoryCreate
from app.api.categories.services import create_category
from ...core.database import get_db

router = APIRouter()

@router.post("/", response_model=Category)
def create_category_endpoint(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db=db, category=category)
