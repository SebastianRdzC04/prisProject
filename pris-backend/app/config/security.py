from datetime import datetime, timedelta
from jose import jwt, JWTError
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

key_secret = os.getenv("JWT_SECRET_KEY")
key_algorithm = os.getenv("JWT_ALGORITHM")

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, key_secret, algorithm=key_algorithm)
    return encoded_jwt

def verify_token(token: str):
    try:
        return jwt.decode(token, key_secret, algorithms=[key_algorithm])
    except JWTError:
        return None