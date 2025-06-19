from fastapi import APIRouter

from backend.track_specific.sports.api.endpoints import players

api_router = APIRouter()
api_router.include_router(players.router, prefix="/players", tags=["players"])