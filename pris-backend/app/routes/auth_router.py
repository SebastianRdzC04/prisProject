from fastapi import APIRouter
from fastapi.params import Depends

from ..schemas.auth_schema import RegisterRequest, LoginResponse, LoginRequest
from ..dependencies.auth_dependencies import get_auth_service
from ..services.auth_service import AuthService
from ..schemas.user_schema import UserRead

router = APIRouter()

@router.post("/register", response_model=UserRead)
async def register_user(
    register_data: RegisterRequest,
    auth_service:AuthService = Depends(get_auth_service)
):
    """
    Register a new user.
    """
    return await auth_service.register(register_data)


@router.post("/login", response_model=LoginResponse)
async def login_user(
    login_data: LoginRequest,
    auth_service:AuthService = Depends(get_auth_service)
):
    """
    Authenticate a user.
    """
    return await auth_service.login(login_data)