from fastapi import APIRouter, Depends
from app.schemas.responses import HealthResponse
from app.schemas.app_config import AppConfigModel
from app.schemas.runtime_config import RuntimeConfigModel, RuntimeConfigUpdateModel
from app.services.runtime_config_service import RuntimeConfigService
from app.dependencies import get_app_config, get_runtime_config_service

router = APIRouter(tags=["configuration"])

@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    return HealthResponse(status="ok")

@router.get("/config/app", response_model=AppConfigModel)
async def get_static_config(
    app_config: AppConfigModel = Depends(get_app_config)
) -> AppConfigModel:
    return app_config

@router.get("/config/runtime", response_model=RuntimeConfigModel)
async def get_runtime_config(
    runtime_service: RuntimeConfigService = Depends(get_runtime_config_service)
) -> RuntimeConfigModel:
    return runtime_service.get_config()

@router.put("/config/runtime", response_model=RuntimeConfigModel)
async def update_runtime_config(
    new_config: RuntimeConfigUpdateModel,
    runtime_service: RuntimeConfigService = Depends(get_runtime_config_service)
) -> RuntimeConfigModel:
    updated_config = runtime_service.update_config(new_config)
    return updated_config