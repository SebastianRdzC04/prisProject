from sqlalchemy.orm import selectinload
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from ..db.models import Admin, User


class AdminRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_admin(self, admin:Admin):
        self.session.add(admin)
        await self.session.commit()
        await self.session.refresh(admin)
        return admin

    async def get_admin_by_id(self, admin_id: str):
        admin = await self.session.execute(
            select(Admin)
            .where(Admin.id == admin_id)
            .where(Admin.is_on == True)
            .options(
                selectinload(Admin.user).selectinload(User.personal_data)
            )
        )
        return admin.scalars().first()

    async def get_all_admins(self):
        admins = await self.session.execute(
            select(Admin)
            .where(Admin.is_on == True)
            .options(
                selectinload(Admin.user).selectinload(User.personal_data)
            )
        )
        return admins.scalars().all()