from sqlalchemy.orm import selectinload
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from ..db.models import Appointment, Client, User


class AppointmentRepository:
    def __init__(self, session:AsyncSession):
        self.session = session

    async def create_appointment(self, appointment: Appointment):
        self.session.add(appointment)
        await self.session.commit()
        await self.session.refresh(appointment)
        return appointment

    async def get_appointment(self, appointment_id: str):
        appointment = await self.session.execute(
            select(Appointment)
            .where(Appointment.id == appointment_id)
            .options(
                selectinload(Appointment.client)
                .selectinload(Client.user)
                .selectinload(User.personal_data),
                selectinload(Appointment.date)
            )
        )
        return appointment.scalars().first()

    async def get_all_appointments(self):
        appointments = await self.session.execute(
            select(Appointment)
            .options(
                selectinload(Appointment.client)
                .selectinload(Client.user)
                .selectinload(User.personal_data),
                selectinload(Appointment.date)
            )
        )
        return appointments.scalars().all()