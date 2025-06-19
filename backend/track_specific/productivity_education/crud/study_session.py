from sqlalchemy.orm import Session
from .base import CRUDBase
from backend.track_specific.productivity_education.models.study_session import StudySession
from backend.track_specific.productivity_education.schemas.study_session import StudySessionCreate, StudySessionUpdate

class CRUDStudySession(CRUDBase[StudySession, StudySessionCreate, StudySessionUpdate]):
    def get_by_user(self, db: Session, *, user_id: int) -> list[StudySession]:
        return db.query(StudySession).filter(StudySession.user_id == user_id).all()

study_session = CRUDStudySession(StudySession)