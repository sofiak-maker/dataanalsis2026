from pydantic import BaseModel

class RuntimeSettingsModel(BaseModel):
    log_level: str = "INFO"
    feature_flag: bool = True
    maintenance_mode: bool = False
    runtime_message: str = "Обычный режим работы"

class RuntimeService:
    """Сервис для работы с изменяемыми параметрами"""
    def __init__(self):
        self.settings = RuntimeSettingsModel()

    def get_settings(self) -> RuntimeSettingsModel:
        return self.settings

    def update_settings(self, new_settings: RuntimeSettingsModel) -> RuntimeSettingsModel:
        self.settings = new_settings
        return self.settings

runtime_service = RuntimeService()