from fastapi import HTTPException
from passlib.context import CryptContext

from ..db.models import User, PersonalData
from ..repositories.user_repository import UserRepository
from ..repositories.personal_data_repository import PersonalDataRepository
from ..schemas.user_schema import UserCreate, UserRead, UserUpdate, UserWithPersonalData
from ..schemas.personal_data_schema import PersonalDataBase, PersonalDataRead, PersonalDataUpdate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService:
    def __init__(self,
                 user_repository:UserRepository,
                 personal_data_repository:PersonalDataRepository):
        self.personal_data_repository = personal_data_repository
        self.user_repository = user_repository

    async def create_user(self, user: UserCreate) -> UserRead:
        password_hashed = pwd_context.hash(user.password)

        user_to_create = User(
            email=user.email,
            password=password_hashed,
        )
        created_user = await self.user_repository.create_user(user_to_create)
        return UserRead.model_validate(created_user)

    async def get_user_by_id(self, user_id:str) -> UserRead:
        user = await self.user_repository.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return UserRead.model_validate(user)

    async def get_user_by_email(self, email:str) -> UserRead:
        user = await self.user_repository.get_user_by_email(email)
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return UserRead.model_validate(user)

    async def delete_user(self, user_id:str) -> UserRead:
        user = await self.user_repository.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        deleted_user = await self.user_repository.delete_user(user)
        return UserRead.model_validate(deleted_user)

    async def get_all_users(self) -> list[UserRead]:
        users = await self.user_repository.get_all_users()
        return [UserRead.model_validate(user) for user in users]

    async def update_user(self, user_id:str, user_update:UserUpdate) -> UserRead:
        user = await self.user_repository.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        user_data = user_update.model_dump(exclude_unset=True)
        for key, value in user_data.items():
            setattr(user, key, value)

        updated_user = await self.user_repository.update_user(user)
        return UserRead.model_validate(updated_user)

    async def create_personal_data(self, user_id:str, personal_data:PersonalDataBase) -> PersonalDataRead:
        user = await self.user_repository.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        personal_data_to_create = PersonalData(
            user_id=user.id,
            first_name=personal_data.first_name,
            last_name=personal_data.last_name,
            birth_date=personal_data.birth_date,
            phone_number=personal_data.phone_number,
            address=personal_data.address
        )
        created_personal_data = await self.personal_data_repository.create_personal_data(
            personal_data_to_create)
        return PersonalDataRead.model_validate(created_personal_data)

    async def get_user_with_personal_data(self, user_id:str) -> UserWithPersonalData:
        user = await self.user_repository.get_user_with_personal_data(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return UserWithPersonalData.model_validate(user)

    async def get_all_users_with_personal_data(self) -> list[UserWithPersonalData]:
        users = await self.user_repository.get_all_users_with_personal_data()
        return [UserWithPersonalData.model_validate(user) for user in users]

    async def update_personal_data(self, user_id:str, personal_data:PersonalDataUpdate) -> PersonalDataRead:
        user = await self.user_repository.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        personal_data_to_update = await self.personal_data_repository.get_personal_data_by_user_id(user_id)
        if not personal_data_to_update:
            raise HTTPException(status_code=404, detail="Datos personales no encontrados")

        personal_data_data = personal_data.model_dump(exclude_unset=True)
        for key, value in personal_data_data.items():
            setattr(personal_data_to_update, key, value)

        updated_personal_data = await self.personal_data_repository.update_personal_data(personal_data_to_update)
        return PersonalDataRead.model_validate(updated_personal_data)




