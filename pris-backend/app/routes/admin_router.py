from fastapi import APIRouter
from fastapi.params import Depends

from ..services.admin_service import AdminService
from ..dependencies.admin_dependencies import get_admin_service
from ..schemas.admin_schema import AdminWithData, AdminRead, AdminCreate


router = APIRouter()

@router.get("/", response_model=list[AdminWithData])
async def get_all_admins(
    admin_service: AdminService = Depends(get_admin_service),
):
    """
    Get all admins.
    """
    return await admin_service.get_all_admins()

@router.get("/{admin_id}", response_model=AdminWithData)
async def get_admin_by_id(
    admin_id: str,
    admin_service: AdminService = Depends(get_admin_service)
):
    """
    Get admin by id.
    """

    return await admin_service.get_admin_by_id(admin_id)

@router.post("/", response_model=AdminRead)
async def create_admin(
    admin: AdminCreate,
    admin_service: AdminService = Depends(get_admin_service)
):
    """
    Create a new admin.
    """

    return await admin_service.create_admin(admin)

@router.get("/user/{user_id}", response_model=AdminWithData)
async def get_admin_by_user_id(
    user_id: str,
    admin_service: AdminService = Depends(get_admin_service)
):
    """
    Get admin by user id.
    """

    return await admin_service.get_admin_by_user_id(user_id)
