from fastapi import HTTPException

from passlib.context import CryptContext

from ..repositories.user_repository import UserRepository
from ..db.models import User
from ..schemas.user_schema import UserRead
from ..schemas.auth_schema import LoginRequest, LoginResponse
from ..config import security
from ..schemas.auth_schema import RegisterRequest

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    def __init__(self, user_repository:UserRepository):
        self.user_repository = user_repository

    async def register(self, register_data:RegisterRequest) -> UserRead :
        """
        Register a new user.
        """
        user_existing = await self.user_repository.get_user_by_email(register_data.email)
        if user_existing:
            raise HTTPException(status_code=400, detail="Email already registered")
        password_hashed = pwd_context.hash(register_data.password)

        new_user = User(
            email=register_data.email,
            password=password_hashed,
        )

        return UserRead.from_orm(await self.user_repository.create_user(new_user))

    async def login(self, login_data:LoginRequest) -> LoginResponse:
        """
        Authenticate a user.
        """
        user = await self.user_repository.get_user_by_email(login_data.email)
        if not user or not pwd_context.verify(login_data.password, user.password):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        payload = {
            "id": str(user.id),
            "email": user.email,
        }

        token = security.create_access_token(payload)

        return LoginResponse(token=token)



