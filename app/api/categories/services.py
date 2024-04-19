from sqlalchemy.orm import Session

from app.api.categories.models import Category
from app.api.categories.schemas import CategoryCreate

def create_category(db: Session, category: CategoryCreate):
    db_category = Category(**category.model_dump())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category
