from fastapi import APIRouter

from backend.track_specific.productivity_education.api.endpoints import study_sessions

api_router = APIRouter()
api_router.include_router(study_sessions.router, prefix="/study_sessions", tags=["study_sessions"])