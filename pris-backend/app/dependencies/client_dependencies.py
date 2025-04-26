from fastapi.params import Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from ..repositories.client_repository import ClientRepository
from ..db.session import get_session
from ..services.client_service import ClientService


def get_client_repository(session: AsyncSession = Depends(get_session)) -> ClientRepository:
    """
    Dependency to get the client repository
    """
    return ClientRepository(session)

def get_client_service(client_repository:ClientRepository = Depends(get_client_repository)) -> ClientService:
    """
    Dependency to get the client service
    """
    return ClientService(client_repository)