from pydantic_settings import BaseSettings
from pathlib import Path
from pydantic import BaseModel


BASE_DIR = Path(__file__).parent.parent


class DBSettings(BaseModel):
    # путь к базе данных
    url: str = f"sqlite+aiosqlite:///{BASE_DIR / "db.sqlite3"}"
    # вывод логирования в консоль
    echo: bool = False


class Setup(BaseModel):
    # ip адрес сервера
    host: str = "127.0.0.1"
    # порт сервера
    port: int = 8000
    # автоперезагрузка сервера
    reload: bool = True


class Settings(BaseSettings):
    # настройки базы данных
    db: DBSettings = DBSettings()
    # настройки сервера
    setup: Setup = Setup()


settings = Settings()
