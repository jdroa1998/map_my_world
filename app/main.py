from fastapi import FastAPI

from .api.locations import locations
from .api.categories import categories
from .api.recommendations import recommendations

app = FastAPI(title="Map My World API", version="1.0")

app.include_router(locations.router, prefix="/api/locations", tags=["locations"])
app.include_router(categories.router, prefix="/api/categories", tags=["categories"])
app.include_router(recommendations.router, prefix="/api/recommendations", tags=["recommendations"])

