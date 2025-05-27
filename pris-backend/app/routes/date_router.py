from fastapi import APIRouter
from fastapi.params import Depends

from ..dependencies.date_dependencies import get_date_service
from ..services.date_service import DateService
from ..schemas.date_schema import DateWithClient, DateCreate, DateRead, DateUpdate



router = APIRouter()

@router.get("/")
async def get_all_dates(date_service: DateService = Depends(get_date_service)):
    """
    Get all dates
    """
    return await date_service.get_all_dates()

@router.get("/{date_id}", response_model=DateWithClient)
async def get_date(date_id: str, date_service: DateService = Depends(get_date_service)):
    """
    Get date by ID
    """
    return await date_service.get_date(date_id)

@router.post("/", response_model=DateRead)
async def create_date(date_create: DateCreate, date_service: DateService = Depends(get_date_service)):
    """
    Create a new date
    """
    return await date_service.create_date(date_create)

@router.put("/{date_id}", response_model=DateRead)
async def update_date(date_id: str, date_update: DateUpdate, date_service: DateService = Depends(get_date_service)):
    """
    Update a date by ID
    """
    return await date_service.update_date(date_id, date_update)

@router.get("/client/{client_id}", response_model=list[DateWithClient])
async def get_dates_by_client(client_id: str, date_service: DateService = Depends(get_date_service)):
    """
    Get all dates for a specific client
    """
    return await date_service.get_dates_by_client(client_id)




