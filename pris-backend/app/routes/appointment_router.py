from fastapi import APIRouter, Depends

from ..dependencies.appointment_dependency import get_appointment_service
from ..services.appointment_service import AppointmentService
from ..schemas.appointment_schema import AppointmentCreate


router = APIRouter()

@router.get("/")
async def get_appointments(appointment_service:AppointmentService=Depends(get_appointment_service)):
    """
    Get all appointments.
    """
    appointments = await appointment_service.get_all_appointments()
    return appointments

@router.get("/{appointment_id}")
async def get_appointment(appointment_id:str, appointment_service:AppointmentService=Depends(get_appointment_service)):
    """
    Get appointment by id.
    """
    appointment = await appointment_service.get_appointment(appointment_id)
    return appointment

@router.post("/")
async def create_appointment(appointment_create:AppointmentCreate, appointment_service:AppointmentService=Depends(get_appointment_service)):
    """
    Create a new appointment.
    """
    appointment = await appointment_service.create_appointment(appointment_create)
    return appointment
