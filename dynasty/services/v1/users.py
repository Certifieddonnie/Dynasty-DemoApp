""" CRUD operations for users """
from sqlalchemy.orm import Session
from models.v1.users import User
from models.schema.users import UserCreate, UserBase
from utils.utils import get_password_hash
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from configs.config import configs
from jose import JWTError, jwt
from utils.utils import get_db, decode_token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_user(db: Session, user_id: str):
    """ Get a user by id """
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    """ Get a user by email """
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    """ Get all users """
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    """ Create a user """
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"id": db_user.id, "email": db_user.email}


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """ Get the current user """
    configs = configs.get("development")
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_token(token)
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user_by_email(db, email=email)
    if user is None:
        raise credentials_exception
    return UserBase(email=user.email)
