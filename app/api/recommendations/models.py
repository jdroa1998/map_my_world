from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class LocationCategoryReview(Base):
    __tablename__ = "location_category_reviewed"
    id = Column(Integer, primary_key=True, index=True)
    location_id = Column(Integer, ForeignKey("locations.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    last_reviewed = Column(DateTime, nullable=True)
    location = relationship("Location")
    category = relationship("Category")
