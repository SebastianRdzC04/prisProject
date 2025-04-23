from uuid import UUID

from pydantic import BaseModel
from ..db.models import AppointmentStatus
from ..schemas.client_schema import ClientWithData
from ..schemas.date_schema import DateRead


class AppointmentBase(BaseModel):
    status: AppointmentStatus = AppointmentStatus.en_proceso

class AppointmentCreate(AppointmentBase):
    client_id: UUID
    date_id: UUID


class AppointmentRead(AppointmentBase):
    id: UUID
    client_id: UUID
    date_id: UUID

    class Config:
        from_attributes = True
        orm_mode = True

class AppointmentWithData(AppointmentRead):
    client_id: UUID
    date_id: UUID

    client: ClientWithData
    date: DateRead
