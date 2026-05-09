from pydantic import BaseModel, Field
from typing import Literal

class RuntimeConfigModel(BaseModel):
    log_level: Literal["INFO", "DEBUG", "WARNING", "ERROR"] = Field(
        default="INFO",
        description="Уровень логирования"
    )
    feature_flag: bool = Field(default=True, description="Флаг новой функции")
    maintenance_mode: bool = Field(default=False, description="Режим обслуживания")
    runtime_message: str = Field(
        default="Приложение работает в штатном режиме",
        description="Сообщение runtime"
    )

class RuntimeConfigUpdateModel(BaseModel):
    log_level: Literal["INFO", "DEBUG", "WARNING", "ERROR"]
    feature_flag: bool
    maintenance_mode: bool
    runtime_message: str