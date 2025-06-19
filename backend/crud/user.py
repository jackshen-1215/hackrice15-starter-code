from sqlalchemy.orm import Session

from core.security import get_password_hash, verify_password
from models.user import User
from schemas.user import UserCreate

def get_user_by_email(db: Session, *, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()

def authenticate(db: Session, *, email: str, password: str) -> User | None:
    user = get_user_by_email(db, email=email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

def get(db: Session, id: int) -> User | None:
    return db.query(User).filter(User.id == id).first()

def create_user(db: Session, *, obj_in: UserCreate) -> User:
    db_obj = User(
        email=obj_in.email,
        hashed_password=get_password_hash(obj_in.password),
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj