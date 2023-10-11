""" CRUD operations for users """
from sqlalchemy.orm import Session
from dynasty.models.v1.users import User
from dynasty.models.schema.users import UserCreate, UserBase
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from dynasty.utils.utils import decode_token, get_password_hash, get_db


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


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
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"id": db_user.id, "email": db_user.email}


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """ Get the current user """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # print("Hello!")
        payload = decode_token(token)
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user_by_email(db=db, email=email)
    if user is None:
        raise credentials_exception
    return user
