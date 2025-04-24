from fastapi import HTTPException

from ..repositories.admin_repository import AdminRepository
from ..schemas.admin_schema import AdminCreate, AdminRead, AdminWithData
from ..db.models import Admin

class AdminService:
    def __init__(self, admiin_repository:AdminRepository):
        self.admin_repository = admiin_repository

    async def create_admin(self, admin:AdminCreate) -> AdminRead:
        admin = Admin(
            user_id=admin.user_id,
        )
        created_admin = await self.admin_repository.create_admin(admin)
        return AdminRead.model_validate(created_admin)

    async def get_admin_by_id(self, admin_id: str) -> AdminWithData:
        admin = await self.admin_repository.get_admin_by_id(admin_id)
        if not admin:
            raise HTTPException(status_code=404, detail="Cliente no encontrado")

        return AdminWithData.model_validate(admin)

    async def get_all_admins(self) -> list[AdminWithData]:
        admins = await self.admin_repository.get_all_admins()
        if not admins:
            raise HTTPException(status_code=404, detail="No hay administradores disponibles")

        return [AdminWithData.model_validate(admin) for admin in admins]