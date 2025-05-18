from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import List, Dict, Optional
from enum import Enum


class AccessLevelEnum(str, Enum):
    client = "client"
    admin = "admin"
    owner = "owner"


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    access_level: AccessLevelEnum = AccessLevelEnum.client


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    balance: float = 0.0
    is_verified: bool = False
    date_of_birth: Optional[datetime] = None
    registration_date: datetime

    class Config:
        orm_mode = True
