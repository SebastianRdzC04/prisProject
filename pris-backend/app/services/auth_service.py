from fastapi import HTTPException

from passlib.context import CryptContext

from ..repositories.user_repository import UserRepository
from ..repositories.client_repository import ClientRepository
from ..db.models import User, Client
from ..schemas.user_schema import UserRead
from ..schemas.client_schema import ClientRead
from ..schemas.auth_schema import LoginRequest, LoginResponse
from ..config import security
from ..schemas.auth_schema import RegisterRequest

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    def __init__(self, user_repository:UserRepository, client_repository:ClientRepository):
        self.user_repository = user_repository
        self.client_repository = client_repository

    async def register(self, register_data:RegisterRequest) -> ClientRead :
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

        user_created = await self.user_repository.create_user(new_user)
        if not user_created:
            raise HTTPException(status_code=500, detail="User creation failed")

        client_existing = await self.client_repository.get_client_by_user_id(user_created.id)
        if client_existing:
            raise HTTPException(status_code=400, detail="User already has a client")

        new_client = Client(
            user_id=user_created.id
        )
        client_created = await self.client_repository.create_client(new_client)
        if not client_created:
            raise HTTPException(status_code=500, detail="Client creation failed")
        return ClientRead.from_orm(client_created)

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

    async def validate_token(self, token:str) -> bool:
        """
        Validate the access token.
        """
        is_valid = security.verify_token(token)
        if not is_valid:
            raise HTTPException(status_code=401, detail="Invalid token")

        return True



