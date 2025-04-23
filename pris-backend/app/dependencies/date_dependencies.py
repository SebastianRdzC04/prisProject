from fastapi.params import Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from ..db.session import get_session
from ..repositories.date_repository import DateRepository
from ..services.date_service import DateService

def get_date_repository(session:AsyncSession = Depends(get_session)) -> DateRepository:
    return DateRepository(session)

def get_date_service(date_repository:DateRepository = Depends(get_date_repository)) -> DateService:
    return DateService(date_repository)
