from fastapi.params import Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from ..db.session import get_session
from ..repositories.user_repository import UserRepository
from ..repositories.personal_data_repository import PersonalDataRepository
from ..services.user_service import UserService


def get_personal_data_repository(session:AsyncSession = Depends(get_session)) -> PersonalDataRepository:
    """
    Dependency to get the PersonalDataRepository instance.
    """
    return PersonalDataRepository(session)

def get_user_repository(session:AsyncSession = Depends(get_session)) -> UserRepository:
    """
    Dependency to get the UserRepository instance.
    """
    return UserRepository(session)

def get_user_service(user_repository:UserRepository = Depends(get_user_repository),
                     personal_data_repository:PersonalDataRepository = Depends(get_personal_data_repository)) -> UserService:
    """
    Dependency to get the UserService instance.
    """
    return UserService(user_repository, personal_data_repository)