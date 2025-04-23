from fastapi import APIRouter, Depends
from ..schemas.client_schema import ClientWithData
from ..services.client_service import ClientService
from ..dependencies.client_dependencies import get_client_service
from ..schemas.client_schema import ClientCreate

router = APIRouter()


@router.get("/", response_model=list[ClientWithData])
async def get_all_clients(client_service: ClientService = Depends(get_client_service)):
    """
    Get all clients
    """
    # Assuming you have a client_service instance available
    return await client_service.get_all_clients()

@router.get("/{client_id}", response_model=ClientWithData)
async def get_client(client_id: str, client_service: ClientService = Depends(get_client_service)):
    """
    Get client by ID
    """
    # Assuming you have a client_service instance available
    return await client_service.get_client(client_id)

@router.post("/", response_model=ClientWithData)
async def create_client(user_id: ClientCreate, client_service: ClientService = Depends(get_client_service)):
    """
    Create a new client
    """
    # Assuming you have a client_service instance available
    return await client_service.create_client(str(user_id.user_id))

