from fastapi import Depends

from ..db.session import get_session
from ..repositories.appointment_repository import AppointmentRepository
from ..services.appointment_service import AppointmentService

def get_appointment_repository(session=Depends(get_session)) -> AppointmentRepository:
    """
    Dependency to get the appointment repository.
    """
    return AppointmentRepository(session)

def get_appointment_service(appointment_repository=Depends(get_appointment_repository)) -> AppointmentService:
    """
    Dependency to get the appointment service.
    """
    return AppointmentService(appointment_repository)