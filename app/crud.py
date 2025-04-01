from sqlalchemy.orm import Session
from passlib.context import CryptContext
from . import models
from .schemas import UserCreate, NeedCreate

# Ініціалізація для хешування паролів
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(
        email=user.email,
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
        hashed_password=hashed_password,
        is_active=True
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_needs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Need).offset(skip).limit(limit).all()

def create_user_need(db: Session, need: NeedCreate, user_id: int):
    db_need = models.Need(**need.dict(), user_id=user_id)
    db.add(db_need)
    db.commit()
    db.refresh(db_need)
    return db_need