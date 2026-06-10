class AppConfig:
    """
    Статическая конфигурация приложения.
    Изменяется ТОЛЬКО при перезапуске сервера.
    """
    def __init__(
        self,
        app_name: str,
        app_version: str,
        app_description: str,
        app_authors: list[str]
    ):
        self.app_name = app_name
        self.app_version = app_version
        self.app_description = app_description
        self.app_authors = app_authors

    def get_config(self) -> dict:
        """Возвращает конфигурацию в виде словаря"""
        return {
            "app_name": self.app_name,
            "app_version": self.app_version,
            "app_description": self.app_description,
            "app_authors": self.app_authors
        }

# Создаём экземпляр конфигурации ПРИ СТАРТЕ
app_config = AppConfig(
    app_name="Laboratory FastAPI App",
    app_version="1.0.0",
    app_description="Учебное приложение с разделением конфигурации",
    app_authors=["Иванов И.И.", "Петров П.П."]
)