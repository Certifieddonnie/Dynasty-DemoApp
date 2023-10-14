""" User Handling Routes """
from fastapi import APIRouter, Depends, HTTPException, status
from dynasty.utils.utils import get_db, verify_password, create_access_token
from dynasty.services.v1.users import create_user, get_user_by_email, get_current_user
from dynasty.models.schema.users import UserCreate, UserBase
from sqlalchemy.orm import Session
from dynasty.models.v1.users import User
from dynasty.configs.config import JWT_ACCESS_TOKEN_EXPIRES, HEADERS
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/auth/register/", status_code=status.HTTP_201_CREATED, tags=["users"], response_model=UserBase)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    """ Register a user """
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)


@router.post("/auth/token/", tags=["users"], status_code=status.HTTP_200_OK)
async def login_user(user: UserCreate, db: Session = Depends(get_db)):
    """ Login a user """
    db_user = get_user_by_email(db, email=user.email)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found", headers={
                            "WWW-Authenticate": "Bearer"})
    if not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect password", headers={
                            "WWW-Authenticate": "Bearer"})
    access_token = create_access_token(
        data={"sub": db_user.email}, expires_delta=JWT_ACCESS_TOKEN_EXPIRES)
    custom_data = {"access_token": access_token, "token_type": "bearer"}
    return JSONResponse(content=custom_data, headers=HEADERS)


@router.get("/user/profile/", status_code=status.HTTP_200_OK, tags=["users"])
async def get_me(current_user: User = Depends(get_current_user)):
    """ Get the current user """
    # return print("Before")
    if current_user:
        # print("After")
        custom_data = {"id": current_user.id, "email": current_user.email}
        return JSONResponse(content=custom_data, headers=HEADERS)
    raise HTTPException(status_code=404, detail="User not found", headers={
                        "WWW-Authenticate": "Bearer"})
