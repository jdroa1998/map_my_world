from sqlalchemy import Column, Integer, Float
from app.core.database import Base

class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True, index=True)
    longitude = Column(Float, index=True)
    latitude = Column(Float, index=True)
