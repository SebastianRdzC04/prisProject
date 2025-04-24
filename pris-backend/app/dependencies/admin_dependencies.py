from fastapi.params import Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from ..repositories.admin_repository import AdminRepository
from ..services.admin_service import AdminService

from ..db.session import get_session

def get_admin_repository(session:AsyncSession = Depends(get_session)) -> AdminRepository:
    """
    Dependency to get the AdminRepository instance.
    """
    return AdminRepository(session)

def get_admin_service(admin_repository:AdminRepository = Depends(get_admin_repository)) -> AdminService:
    """
    Dependency to get the AdminService instance.
    """
    return AdminService(admin_repository)