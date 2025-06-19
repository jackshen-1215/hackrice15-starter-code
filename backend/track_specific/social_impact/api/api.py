from fastapi import APIRouter
from backend.track_specific.social_impact.api.endpoints import resources

api_router = APIRouter()
api_router.include_router(resources.router, prefix="/resources", tags=["resources"])