from app.schemas.app_config import AppConfigModel
from app.schemas.runtime_config import RuntimeConfigModel
from app.services.runtime_config_service import RuntimeConfigService

def init_dependencies() -> dict:
    app_config = AppConfigModel(
        app_name="Laboratory FastAPI App",
        app_version="1.0.0",
        app_description="Учебное приложение на FastAPI с DI и Pydantic",
        app_authors=["Иванов И.И.", "Петров П.П."]
    )

    initial_runtime_config = RuntimeConfigModel(
        log_level="INFO",
        feature_flag=True,
        maintenance_mode=False,
        runtime_message="Приложение работает в штатном режиме"
    )

    runtime_service = RuntimeConfigService(initial_runtime_config)

    dependencies = {
        "app_config": app_config,
        "runtime_config_service": runtime_service,
    }

    return dependencies