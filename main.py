from fastapi import FastAPI
from core import settings


app = FastAPI()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app="main:app",
        reload=settings.setup.reload,
        host=settings.setup.host,
        port=settings.setup.port,
    )
