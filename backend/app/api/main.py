from datetime import datetime
from fastapi import APIRouter

from app.api.routes import tasks, auth, users, utils
from app.state import state

api_router = APIRouter()
api_router.include_router(auth.router, tags=["login", "auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])

# TODO: i need to consolidate these endpoints

api_router.get("/")
def version() -> str:
    return "0.0.1"

api_router.get("/health")
def health() -> str:
    return "ok"

api_router.get("/status", tags=["meta"])
def get_status() -> dict:
    return {
        "status": state.status,
        "uptime": (datetime.utcnow() - state.backend_start).total_seconds(),
    }

api_router.get("/info", tags=["meta"])
def get_info() -> dict:
    return {
        "service": "Web2 App Backend",
        "version": "0.0.1",
        "status": state.status,
        "uptime": (datetime.utcnow() - state.backend_start).total_seconds(),
    }

@api_router.get("/time")
def get_current_time() -> dict:
    """Endpoint to get the current server time."""
    return {"current_time": datetime.utcnow().isoformat()}

@api_router.get("/config")
def get_config() -> dict:
    """Endpoint to get the current configuration settings."""
    return {
        "email_enabled": settings.emails_enabled,
        "smtp_host": settings.SMTP_HOST,
        "smtp_port": settings.SMTP_PORT
    }

