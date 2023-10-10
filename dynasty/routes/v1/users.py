""" User Handling Routes """
from fastapi import APIRouter, Depends, HTTPException, status
from utils.utils import get_db, verify_password, create_access_token
from services.v1.users import create_user, get_user_by_email, get_current_user
from models.schema.users import UserCreate, UserBase
from sqlalchemy.orm import Session
from models.v1.users import User
from configs.config import configs

configs = configs.get("development")

router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED, tags=["users"], response_model=UserBase)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    """ Register a user """
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)


@router.post("/login", tags=["users"], status_code=status.HTTP_200_OK)
async def login_user(user: UserCreate, db: Session = Depends(get_db)):
    """ Login a user """
    db_user = get_user_by_email(db, email=user.email)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found", headers={
                            "WWW-Authenticate": "Bearer"})
    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Incorrect password", headers={
                            "WWW-Authenticate": "Bearer"})
    access_token = create_access_token(
        data={"sub": db_user.email}, expires_delta=configs.JWT_ACCESS_TOKEN_EXPIRES)
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", tags=["users"], status_code=status.HTTP_200_OK)
async def get_me(current_user: UserBase = Depends(get_current_user)):
    """ Get the current user """
    if current_user:
        return current_user
    raise HTTPException(status_code=404, detail="User not found", headers={
                        "WWW-Authenticate": "Bearer"})
