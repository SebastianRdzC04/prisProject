from uuid import UUID

from pydantic import BaseModel
from ..schemas.personal_data_schema import PersonalDataRead


class UserBase(BaseModel):
    email:str

class UserCreate(UserBase):
    password:str

class UserRead(UserBase):
    id:UUID

    class Config:
        from_attributes = True

class UserUpdate(UserBase):
    email:str | None = None

class UserWithPersonalData(UserRead):
    personal_data: PersonalDataRead | None = None
