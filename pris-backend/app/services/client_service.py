from fastapi import HTTPException

from ..repositories.client_repository import ClientRepository
from ..schemas.client_schema import ClientWithData
from ..db.models import Client


class ClientService:
    def __init__(self, client_repository:ClientRepository):
        self.client_repository = client_repository

    async def create_client(self, user_id:str) -> ClientWithData :
        client_create = Client(
            user_id=user_id,
            is_on=True,
        )
        await self.client_repository.create_client(client_create)
        client = await self.client_repository.get_client_by_id(client_create.id)
        if not client:
            raise HTTPException(status_code=404, detail="Error al crear el cliente")

        return ClientWithData.from_orm(client)

    async def get_client(self, client_id: str) -> ClientWithData:
        client = await self.client_repository.get_client_by_id(client_id)
        if not client:
            raise HTTPException(status_code=404, detail="Cliente no encontrado")

        return ClientWithData.from_orm(client)

    async def get_all_clients(self) -> list[ClientWithData]:
        clients = await self.client_repository.get_all_clients()
        if not clients:
            raise HTTPException(status_code=404, detail="No hay clientes disponibles")

        return [ClientWithData.from_orm(client) for client in clients]

