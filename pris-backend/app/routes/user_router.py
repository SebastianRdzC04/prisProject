from fastapi import APIRouter
from fastapi.params import Depends

from ..dependencies.user_dependencies import get_user_service
from ..schemas.user_schema import UserRead, UserUpdate, UserWithPersonalData, UserCreate
from ..services.user_service import UserService
from ..schemas.personal_data_schema import PersonalDataBase, PersonalDataRead, PersonalDataUpdate

router = APIRouter()

@router.post("/", response_model=UserRead)
async def create_user(user:UserCreate, user_service:UserService = Depends(get_user_service)):
    """
    Endpoint to create a user.
    """
    return await user_service.create_user(user)

@router.get("/all", response_model=list[UserRead])
async def get_all_users(user_service:UserService = Depends(get_user_service)):
    """
    Endpoint to get all users.
    """
    return await user_service.get_all_users()


@router.get("/{user_id}", response_model=UserRead)
async def get_user_by_id(user_id:str, user_service:UserService = Depends(get_user_service)):
    """
    Endpoint to get a user by ID.
    """
    return await user_service.get_user_by_id(user_id)

@router.get("/email/{email}", response_model=UserRead)
async def get_user_by_email(email:str, user_service:UserService = Depends(get_user_service)):
    """
    Endpoint to get a user by email.
    """
    return await user_service.get_user_by_email(email)

@router.put("/{user_id}", response_model=UserRead)
async def update_user(user_id:str, user:UserUpdate, user_service:UserService = Depends(get_user_service)):
    """
    Endpoint to update a user.
    """
    return await user_service.update_user(user_id, user)

@router.delete("/{user_id}", response_model=UserRead)
async def delete_user(user_id:str, user_service:UserService = Depends(get_user_service)):
    """
    Endpoint to delete a user.
    """
    return await user_service.delete_user(user_id)

@router.get("/all/personal_data", response_model=list[UserWithPersonalData])
async def get_all_users_with_personal_data(user_service:UserService = Depends(get_user_service)):
    """
    Endpoint to get all users with their personal data.
    """
    return await user_service.get_all_users_with_personal_data()

@router.post("/{user_id}/personal_data", response_model=PersonalDataRead)
async def create_personal_data(user_id:str, personal_data:PersonalDataBase, user_service:UserService = Depends(get_user_service)):
    """
    Endpoint to create personal data for a user.
    """
    return await user_service.create_personal_data(user_id, personal_data)

@router.get("/{user_id}/personal_data", response_model=UserWithPersonalData)
async def get_user_with_personal_data(user_id:str, user_service:UserService = Depends(get_user_service)):
    """
    Endpoint to get a user with their personal data.
    """
    return await user_service.get_user_with_personal_data(user_id)

@router.put("/{user_id}/personal_data", response_model=PersonalDataRead)
async def update_personal_data(user_id:str, personal_data:PersonalDataUpdate, user_service:UserService = Depends(get_user_service)):
    """
    Endpoint to update personal data for a user.
    """
    return await user_service.update_personal_data(user_id, personal_data)

