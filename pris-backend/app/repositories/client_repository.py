from sqlalchemy.orm import selectinload
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from ..db.models import Client, User


class ClientRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_client(self, client):
        self.session.add(client)
        await self.session.commit()
        await self.session.refresh(client)
        return client

    async def get_client_by_id(self, client_id: str):
        client = await self.session.execute(
            select(Client)
            .where(Client.id == client_id)
            .where(Client.is_on == True)
            .options(
                selectinload(Client.user).selectinload(User.personal_data)
            )
        )
        return client.scalars().first()

    async def get_all_clients(self):
        clients = await self.session.execute(
            select(Client)
            .where(Client.is_on == True)
            .options(
                selectinload(Client.user).selectinload(User.personal_data)
            )
        )
        return clients.scalars().all()

    async def get_client_by_user_id(self, user_id: str):
        client = await self.session.execute(
            select(Client)
            .where(Client.user_id == user_id)
            .where(Client.is_on == True)
        )
        return client.scalars().first()