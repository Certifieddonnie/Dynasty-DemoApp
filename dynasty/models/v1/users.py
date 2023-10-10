"""
User Models
"""
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import os
from uuid import uuid4

from database.database import Base


class User(Base):
    """ Model for Users"""

    __tablename__ = "users"
    id = Column(
        String(50), primary_key=True, index=True, default=lambda: str(uuid4()), unique=True
    )
    email = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(100))
    is_active = Column(Boolean(), default=True)

    # Relationships


# class Token(Base):
#     access_token: str
#     token_type: str


# class TokenData(Base):
#     username: str | None = None
