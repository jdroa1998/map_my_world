from pydantic import BaseModel

class CategoryCreate(BaseModel):
    name: str

class Category(BaseModel):
    name: str
    id: int