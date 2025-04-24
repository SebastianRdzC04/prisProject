from uuid import UUID
from ..schemas.user_schema import UserWithPersonalData

from pydantic import BaseModel


class ClientBase(BaseModel):
    user_id: UUID

class ClientCreate(ClientBase):
    pass

class ClientRead(ClientBase):
    id: UUID

    class Config:
        from_attributes = True

class ClientWithData(ClientRead):
    user: UserWithPersonalData