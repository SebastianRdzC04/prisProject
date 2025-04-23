from fastapi.params import Depends

from ..repositories.user_repository import UserRepository
from .user_dependencies import get_user_repository
from ..services.auth_service import AuthService


def get_auth_service(user_repository: UserRepository = Depends(get_user_repository)) -> AuthService:
    """
    Dependency to get the AuthService instance.
    """
    return AuthService(user_repository=user_repository)