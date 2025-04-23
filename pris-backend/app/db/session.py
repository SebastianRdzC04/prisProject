from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from pathlib import Path

# Obtener la ruta absoluta al directorio raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
# Ruta al archivo .env
ENV_PATH = os.path.join(BASE_DIR, "docker", ".env")

# Verificar si el archivo existe
if not os.path.exists(ENV_PATH):
    raise FileNotFoundError(f"El archivo .env no se encontró en: {ENV_PATH}")

# Cargar .env
load_dotenv(ENV_PATH)

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