
from pydantic import BaseModel

import datetime
from uuid import UUID

from ..db.models import DateType, DateStatus
from ..schemas.client_schema import ClientWithData


class DateBase(BaseModel):
    type: DateType
    date: datetime.date
    time: datetime.time

class DateCreate(DateBase):
    client_id: UUID

class DateRead(DateBase):
    id: UUID
    client_id: UUID
    status: DateStatus

    class Config:
        from_attributes = True

class DateUpdate(DateBase):
    type: DateType | None = None
    status: DateStatus | None = None
    date: datetime.date | None = None
    time: datetime.time | None = None

class DateWithClient(DateRead):
    client: ClientWithData