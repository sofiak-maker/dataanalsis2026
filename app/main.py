from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.dependencies import get_dependencies
from app.routes import config_routes

@asynccontextmanager
async def lifespan(app: FastAPI):
    deps = get_dependencies()
    print("Зависимости инициализированы")
    print(f"Приложение: {deps['app_config'].app_name}")
    yield
    print("Приложение завершает работу")

app = FastAPI(
    title="FastAPI App with Pydantic & DI",
    description="Лабораторная работа №6: Pydantic и Dependency Injection",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(config_routes.router)

@app.get("/")
async def root():
    return RedirectResponse(url="/docs")

@app.get("/ping")
async def ping():
    return "pong"