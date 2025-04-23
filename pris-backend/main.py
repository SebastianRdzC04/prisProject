from fastapi import FastAPI
from app.routes import auth_router
from app.routes import user_router
from app.routes import client_router
from app.routes import date_router
from app.routes import appointment_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router.router, prefix="/auth", tags=["Auth Routes"])
app.include_router(user_router.router, prefix="/users", tags=["User Routes"])
app.include_router(client_router.router, prefix="/clients", tags=["Client Routes"])
app.include_router(date_router.router, prefix="/dates", tags=["Date Routes"])
app.include_router(appointment_router.router, prefix="/appointments", tags=["Appointment Routes"])

