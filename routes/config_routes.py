from fastapi import APIRouter
from config import app_config
from runtime_service import runtime_service, RuntimeSettingsModel
router = APIRouter()
@router.get("/config/app")
async def get_static_config():
    return app_config.get_config()
@router.get("/config/runtime")
async def get_runtime_config():
    return runtime_service.get_settings().dict()
@router.put("/config/runtime")
async def update_runtime_config(new_config: RuntimeSettingsModel):
    updated = runtime_service.update_settings(new_config)
    return updated.dict()
