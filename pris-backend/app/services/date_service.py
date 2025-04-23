from fastapi import HTTPException

from ..repositories.date_repository import DateRepository
from ..schemas.date_schema import DateCreate, DateRead, DateWithClient, DateUpdate
from ..db.models import Date

class DateService:

    def __init__(self, date_repository:DateRepository):
        self.date_repository = date_repository

    async def create_date(self, date_create:DateCreate) -> DateRead:
        date_to_create = Date(
            type=date_create.type,
            date=date_create.date,
            time=date_create.time,
            client_id=date_create.client_id,
        )

        date = await self.date_repository.create_date(date_to_create)
        if not date:
            raise HTTPException(status_code=404, detail="Error al crear la fecha")

        return DateRead.from_orm(date)

    async def get_all_dates(self) -> list[DateWithClient]:
        dates = await self.date_repository.get_all_dates()
        if not dates:
            raise HTTPException(status_code=404, detail="No hay fechas disponibles")

        return [DateWithClient.from_orm(date) for date in dates]

    async def get_date(self, date_id:str) -> DateWithClient:
        date = await self.date_repository.get_date(date_id)
        if not date:
            raise HTTPException(status_code=404, detail="Fecha no encontrada")

        return DateWithClient.from_orm(date)

    async def update_date(self, date_id:str, date_update:DateUpdate) -> DateRead:
        date = await self.date_repository.get_date(date_id)
        if not date:
            raise HTTPException(status_code=404, detail="Fecha no encontrada")

        date_data = date.dict(exclude_unset=True)
        date_data.update(date_update.dict(exclude_unset=True))

        for key, value in date_data.items():
            setattr(date, key, value)

        updated_date = await self.date_repository.update_date(date)
        if not updated_date:
            raise HTTPException(status_code=404, detail="Error al actualizar la fecha")

        return DateRead.from_orm(updated_date)




