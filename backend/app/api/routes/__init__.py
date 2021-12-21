from fastapi import APIRouter
from app.api.routes.routes import router as routes

router = APIRouter()

router.include_router(routes, prefix="/api", tags=["API"])