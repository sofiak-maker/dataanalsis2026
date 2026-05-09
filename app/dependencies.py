from fastapi import Depends
from app.init_dependencies import init_dependencies
from app.schemas.app_config import AppConfigModel
from app.services.runtime_config_service import RuntimeConfigService
_dependencies = None
def get_dependencies():
    global _dependencies
    if _dependencies is None:
        _dependencies = init_dependencies()
    return _dependencies
def get_app_config(deps: dict = Depends(get_dependencies)) -> AppConfigModel:
    return deps["app_config"]
def get_runtime_config_service(deps: dict = Depends(get_dependencies)) -> RuntimeConfigService:
    return deps["runtime_config_service"]