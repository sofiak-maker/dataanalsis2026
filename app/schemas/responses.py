from pydantic import BaseModel, Field

class HealthResponse(BaseModel):
    status: str = Field(default="ok", description="Статус приложения")

    class Config:
        json_schema_extra = {
            "example": {
                "status": "ok"
            }
        }