from pydantic_settings import BaseSettings
from pydantic import BaseModel


class Setup(BaseModel):
    # ip адрес сервера
    host: str = "127.0.0.1"
    # порт сервера
    port: int = 8000
    # автоперезагрузка сервера
    reload: bool = True


class Settings(BaseSettings):
    # настройки сервера
    setup: Setup = Setup()


settings = Settings()
