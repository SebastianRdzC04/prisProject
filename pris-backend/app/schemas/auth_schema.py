import datetime

from pydantic import BaseModel

class RegisterRequest(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str
    birth_date: datetime.date
    phone_number: str
    address: str

class LoginRequest(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
    token: str