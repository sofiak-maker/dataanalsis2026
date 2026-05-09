from fastapi import FastAPI
from config import app_config
from routes import health, config_routes
app = FastAPI(
    title=app_config.app_name,
    version=app_config.app_version,
    description=app_config.app_description
)

app.include_router(health.router)
app.include_router(config_routes.router)

@app.get("/")
def root():
    return {
        "message": f"Добро пожаловать в {app_config.app_name}",
        "docs": "/docs"
    }
