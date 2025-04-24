from uuid import UUID

from pydantic import BaseModel
from .user_schema import UserWithPersonalData


class AdminBase(BaseModel):
    user_id: UUID

class AdminCreate(AdminBase):
    pass

class AdminRead(AdminBase):
    id: UUID

    class Config:
        from_attributes = True


class AdminWithData(AdminRead):
    user: UserWithPersonalData