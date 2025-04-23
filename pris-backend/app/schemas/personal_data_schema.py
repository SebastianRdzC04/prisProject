from datetime import date
from uuid import UUID

from pydantic import BaseModel


class PersonalDataBase(BaseModel):
    first_name:str
    last_name:str
    birth_date:date
    phone_number:str
    address:str

class PersonalDataCreate(PersonalDataBase):
    user_id:UUID

class PersonalDataUpdate(PersonalDataBase):
    first_name:str | None = None
    last_name:str | None = None
    birth_date:date | None = None
    phone_number:str | None = None
    address:str | None = None

class PersonalDataRead(PersonalDataBase):
    class Config:
        from_attributes = True
        orm_mode = True