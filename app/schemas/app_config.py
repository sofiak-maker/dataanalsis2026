from pydantic import BaseModel, Field
from typing import List

class AppConfigModel(BaseModel):
    app_name: str = Field(..., description="Название приложения")
    app_version: str = Field(..., description="Версия приложения")
    app_description: str = Field(..., description="Описание приложения")
    app_authors: List[str] = Field(..., description="Авторы приложения")

    class Config:
        json_schema_extra = {
            "example": {
                "app_name": "Laboratory FastAPI App",
                "app_version": "1.0.0",
                "app_description": "Учебное приложение на FastAPI",
                "app_authors": ["Иванов И.И.", "Петров П.П."]
            }
        }