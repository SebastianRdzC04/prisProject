from fastapi import HTTPException

from ..db.models import Appointment
from ..repositories.appointment_repository import AppointmentRepository
from ..schemas.appointment_schema import AppointmentCreate, AppointmentWithData, AppointmentRead

class AppointmentService:
    def __init__(self, appointment_repository:AppointmentRepository):
        self.appointment_repository = appointment_repository

    async def create_appointment(self, appointment_create:AppointmentCreate) -> AppointmentRead:
        appointment_to_create = Appointment(
            client_id=appointment_create.client_id,
            date_id=appointment_create.date_id
        )

        appointment = await self.appointment_repository.create_appointment(appointment_to_create)
        if not appointment:
            raise HTTPException(status_code=404, detail="Error al crear la cita")

        return AppointmentRead.model_validate(appointment)

    async def get_appointment(self, appointment_id:str) -> AppointmentWithData:
        appointment = await self.appointment_repository.get_appointment(appointment_id)
        if not appointment:
            raise HTTPException(status_code=404, detail="Cita no encontrada")

        return AppointmentWithData.model_validate(appointment)


    async def get_all_appointments(self) -> list[AppointmentWithData]:
        appointments = await self.appointment_repository.get_all_appointments()
        if not appointments:
            raise HTTPException(status_code=404, detail="No hay citas disponibles")

        return [AppointmentWithData.model_validate(appointment) for appointment in appointments]
