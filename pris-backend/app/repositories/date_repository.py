from sqlalchemy.orm import selectinload
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from ..db.models import Date, Client, User


class DateRepository:
    def __init__(self, session:AsyncSession):
        self.session = session

    async def get_date(self, date_id:str):
        date = await self.session.execute(
            select(Date)
            .where(Date.id == date_id)
            .where(Date.is_on == True)
            .options(
                selectinload(Date.client)
                .selectinload(Client.user)
                .selectinload(User.personal_data)
            )
        )
        return date.scalars().first()

    async def create_date(self, date:Date):
        self.session.add(date)
        await self.session.commit()
        await self.session.refresh(date)
        return date

    async def get_all_dates(self):
        dates = await self.session.execute(
            select(Date)
            .where(Date.is_on == True)
            .options(
                selectinload(Date.client)
                .selectinload(Client.user)
                .selectinload(User.personal_data)
            )
        )
        return dates.scalars().all()

    async def delete_date(self, date:Date):
        date.is_on = False
        self.session.add(date)
        await self.session.commit()
        await self.session.refresh(date)
        return date

    async def update_date(self, date:Date):
        self.session.add(date)
        await self.session.commit()
        await self.session.refresh(date)
        return date

    async def get_dates_by_client(self, client_id:str):
        dates = await self.session.execute(
            select(Date)
            .where(Date.client_id == client_id)
            .where(Date.is_on == True)
            .options(
                selectinload(Date.client)
                .selectinload(Client.user)
                .selectinload(User.personal_data)
            )
        )
        return dates.scalars().all()
