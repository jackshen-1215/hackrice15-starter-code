from fastapi import APIRouter

from backend.track_specific.healthcare.api.endpoints import appointments

api_router = APIRouter()
api_router.include_router(appointments.router, prefix="/appointments", tags=["appointments"])