from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from ..db.models import PersonalData


class PersonalDataRepository:
    def __init__(self, session:AsyncSession):
        self.session = session

    async def create_personal_data(self, personal_data:PersonalData):
        self.session.add(personal_data)
        await self.session.commit()
        await self.session.refresh(personal_data)
        return personal_data

    async def get_personal_data_by_user_id(self, user_id:str):
        personal_data = await self.session.execute(
            select(PersonalData)
            .where(PersonalData.user_id == user_id)
        )
        return personal_data.scalars().first()

    async def update_personal_data(self, personal_data:PersonalData):
        self.session.add(personal_data)
        await self.session.commit()
        await self.session.refresh(personal_data)
        return personal_data

    async def delete_personal_data(self, personal_data:PersonalData):
        await self.session.delete(personal_data)
        await self.session.commit()
        return personal_data