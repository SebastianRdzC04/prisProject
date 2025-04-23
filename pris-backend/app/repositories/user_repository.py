from sqlalchemy.orm import selectinload
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from ..db.models import User

class UserRepository:
    def __init__(self, session:AsyncSession):
        self.session = session

    async def create_user(self, user:User):
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def get_user_by_id(self, user_id:str):
        user = await self.session.execute(
            select(User)
            .where(User.id == user_id)
            .where(User.is_on == True)
        )
        return user.scalars().first()

    async def get_user_by_email(self, email:str):
        user = await self.session.execute(
            select(User)
            .where(User.email == email)
            .where(User.is_on == True)
        )
        return user.scalars().first()

    async def delete_user(self, user:User):
        user.is_on = False
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def get_all_users(self):
        users = await self.session.execute(
            select(User)
            .where(User.is_on == True)
        )
        return users.scalars().all()

    async def update_user(self, user:User):
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def get_user_with_personal_data(self, user_id: str):
        result = await self.session.execute(
            select(User)
            .where(User.id == user_id)
            .where(User.is_on == True)
            .options(selectinload(User.personal_data))
        )
        return result.scalars().first()

    async def get_all_users_with_personal_data(self):
        result = await self.session.execute(
            select(User)
            .where(User.is_on == True)
            .options(selectinload(User.personal_data))
        )
        return result.scalars().all()
