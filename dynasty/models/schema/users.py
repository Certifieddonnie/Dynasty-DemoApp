""" Pydantic Models for Users(Schemas) """
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """ Base Model for Users """

    email: EmailStr


class UserCreate(UserBase):
    """ Model for Creating Users """

    password: str


class User(UserBase):
    """ Model for Users """

    id: str
    is_active: bool

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": "1",
                "email": "example@example.com",
            }
        }
