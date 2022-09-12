from pydantic import BaseModel, Field, EmailStr

from typing import Optional


class UserBase(BaseModel):
    name: Optional[str] = Field(alias='user_name')
    age: Optional[int] = None
    email: Optional[EmailStr] = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class UserCreate(UserBase):
    name: str
    age: int = Field(ge=0, le=100)
    email: EmailStr


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: int


class UserName(BaseModel):
    name: str = Field(alias='user_name')

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
