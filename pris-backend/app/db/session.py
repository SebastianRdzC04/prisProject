from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from pathlib import Path


load_dotenv()

# Obtener la URL de la base de datos
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL no está definida en el archivo .env")

# Crear el engine asíncrono
engine = create_async_engine(DATABASE_URL, echo=True)

# Crear la fábrica de sesiones asíncronas
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# Dependencia para usar en FastAPI
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session