from sqlalchemy.orm import Session
from .base import CRUDBase
from backend.track_specific.sports.models.player import Player
from backend.track_specific.sports.schemas.player import PlayerCreate, PlayerUpdate

class CRUDPlayer(CRUDBase[Player, PlayerCreate, PlayerUpdate]):
    def get_by_name(self, db: Session, *, name: str) -> Player:
        return db.query(Player).filter(Player.name == name).first()

player = CRUDPlayer(Player)