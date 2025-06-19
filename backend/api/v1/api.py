from fastapi import APIRouter

from backend.api.v1.endpoints import users
from backend.track_specific.social_impact.api import api as social_impact_api
from backend.track_specific.sports.api import api as sports_api
from backend.track_specific.healthcare.api import api as healthcare_api
from backend.track_specific.productivity_education.api import api as productivity_education_api
from backend.track_specific.entrepreneurship.api import api as entrepreneurship_api

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])

# Include track-specific routers
track_specific_router = APIRouter()
track_specific_router.include_router(social_impact_api.api_router, prefix="/social_impact")
track_specific_router.include_router(sports_api.api_router, prefix="/sports")
track_specific_router.include_router(healthcare_api.api_router, prefix="/healthcare")
track_specific_router.include_router(productivity_education_api.api_router, prefix="/productivity_education")
track_specific_router.include_router(entrepreneurship_api.api_router, prefix="/entrepreneurship")

api_router.include_router(track_specific_router, prefix="/track_specific")