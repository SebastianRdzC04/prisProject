from datetime import date, time, datetime
from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel
import uuid
from enum import Enum
from sqlalchemy import Enum as SQLAlchemyEnum, Column


# Definición de Enums
class DateType(str, Enum):
    consulta = "consulta"
    seguimineot = "seguimiento"


class DateStatus(str, Enum):
    pendiente = "pendiente"
    confirmada = "confirmada"
    cancelada = "cancelada"
    finalizada = "finalizada"


class AppointmentStatus(str, Enum):
    en_proceso = "en proceso"
    finalizada = "finalizada"


class TreatmentStatus(str, Enum):
    en_proceso = "en proceso"
    finalizado = "finalizado"
    cancelado = "cancelado"


# Definición de modelos
class User(SQLModel, table=True):
    __tablename__ = "users"

    id: Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True
    )
    email: str
    password: str
    is_on: bool = True

    # Relaciones
    personal_data: Optional["PersonalData"] = Relationship(back_populates="user")
    admin: Optional["Admin"] = Relationship(back_populates="user")
    client: Optional["Client"] = Relationship(back_populates="user")
    worker: Optional["Worker"] = Relationship(back_populates="user")
    treatments: List["Treatment"] = Relationship(back_populates="user")


class PersonalData(SQLModel, table=True):
    __tablename__ = "personal_data"

    id: Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True
    )
    user_id: uuid.UUID = Field(foreign_key="users.id")
    first_name: str
    last_name: str
    birth_date: date
    phone_number: str
    address: str

    user: Optional[User] = Relationship(back_populates="personal_data")


class Admin(SQLModel, table=True):
    __tablename__ = "admins"

    id: Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True
    )
    user_id: uuid.UUID = Field(foreign_key="users.id")
    is_on: bool = True

    user: Optional[User] = Relationship(back_populates="admin")


class Client(SQLModel, table=True):
    __tablename__ = "clients"

    id: Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True
    )
    user_id: uuid.UUID = Field(foreign_key="users.id")
    is_on: bool = True

    user: Optional[User] = Relationship(back_populates="client")
    histories: List["History"] = Relationship(back_populates="client")
    dates: List["Date"] = Relationship(back_populates="client")
    appointments: List["Appointment"] = Relationship(back_populates="client")


class Worker(SQLModel, table=True):
    __tablename__ = "workers"

    id: Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True
    )
    user_id: uuid.UUID = Field(foreign_key="users.id")
    is_on: bool = True

    user: Optional[User] = Relationship(back_populates="worker")


class Machine(SQLModel, table=True):
    __tablename__ = "machines"

    id: Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True
    )
    name: str
    is_on: bool = True

    histories: List["History"] = Relationship(back_populates="machine")
    treatment_details: List["TreatmentDetail"] = Relationship(back_populates="machine")


class History(SQLModel, table=True):
    __tablename__ = "history"

    id: Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True
    )
    machine_id: uuid.UUID = Field(foreign_key="machines.id")
    client_id: uuid.UUID = Field(foreign_key="clients.id")
    action: str
    timestamp: datetime = Field(default_factory=datetime.now)

    machine: Optional[Machine] = Relationship(back_populates="histories")
    client: Optional[Client] = Relationship(back_populates="histories")


class Date(SQLModel, table=True):
    __tablename__ = "dates"

    id: Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True
    )
    client_id: uuid.UUID = Field(foreign_key="clients.id")
    type: DateType = Field(sa_column=Column("type", SQLAlchemyEnum(DateType, name="date_types")))
    status: DateStatus = Field(default=DateStatus.pendiente, sa_column=Column("status", SQLAlchemyEnum(DateStatus.pendiente, name="date_status")))
    date: date
    time: time
    is_on: bool = True

    client: Optional[Client] = Relationship(back_populates="dates")
    appointment: Optional["Appointment"] = Relationship(back_populates="date")
    treatment_details: List["TreatmentDetail"] = Relationship(back_populates="date")


class Appointment(SQLModel, table=True):
    __tablename__ = "appointments"

    id: Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True
    )
    client_id: uuid.UUID = Field(foreign_key="clients.id")
    date_id: uuid.UUID = Field(foreign_key="dates.id")
    status: AppointmentStatus = Field(default=AppointmentStatus.en_proceso , sa_column=Column("status", SQLAlchemyEnum(AppointmentStatus.en_proceso, name="appoitment_status")))
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    client: Optional[Client] = Relationship(back_populates="appointments")
    date: Optional[Date] = Relationship(back_populates="appointment")


class Treatment(SQLModel, table=True):
    __tablename__ = "treatments"

    id: Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True
    )
    user_id: uuid.UUID = Field(foreign_key="users.id")
    name: str
    description: str
    duration: int
    status: TreatmentStatus = TreatmentStatus.en_proceso
    price: int
    is_on: bool = True

    user: Optional[User] = Relationship(back_populates="treatments")
    treatment_details: List["TreatmentDetail"] = Relationship(back_populates="treatment")


class TreatmentDetail(SQLModel, table=True):
    __tablename__ = "treatment_details"

    id: Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True
    )
    date_id: uuid.UUID = Field(foreign_key="dates.id")
    treatment_id: uuid.UUID = Field(foreign_key="treatments.id")
    machine_id: uuid.UUID = Field(foreign_key="machines.id")
    session_number: int
    is_on: bool = True

    date: Optional[Date] = Relationship(back_populates="treatment_details")
    treatment: Optional[Treatment] = Relationship(back_populates="treatment_details")
    machine: Optional[Machine] = Relationship(back_populates="treatment_details")