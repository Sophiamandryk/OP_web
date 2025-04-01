from pydantic import BaseModel, EmailStr
from typing import Optional

class TokenData(BaseModel):
    username: Optional[str] = None

class UserBase(BaseModel):
    email: EmailStr
    username: str

class UserCreate(UserBase):
    password: str
    first_name: str
    last_name: str

class User(UserBase):
    id: int
    first_name: str
    last_name: str
    is_active: bool

    class Config:
        from_attributes = True

class NeedBase(BaseModel):
    title: str
    description: str

class NeedCreate(NeedBase):
    pass

class Need(NeedBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True