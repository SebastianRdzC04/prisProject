from fastapi.params import Depends

from ..repositories.user_repository import UserRepository
from .user_dependencies import get_user_repository
from ..services.auth_service import AuthService
from ..repositories.client_repository import ClientRepository
from ..repositories.admin_repository import AdminRepository
from .client_dependencies import get_client_repository
from .admin_dependencies import get_admin_repository


def get_auth_service(user_repository: UserRepository = Depends(get_user_repository),
                     client_repository:ClientRepository = Depends(get_client_repository),
                     admin_repository:AdminRepository = Depends(get_admin_repository)) -> AuthService:
    """
    Dependency to get the AuthService instance.
    """
    return AuthService(user_repository, client_repository, admin_repository)