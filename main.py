from contextlib import asynccontextmanager
from fastapi import FastAPI
from core import settings, db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_helper.engine.dispose()


app = FastAPI(lifespan=lifespan)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app="main:app",
        reload=settings.setup.reload,
        host=settings.setup.host,
        port=settings.setup.port,
    )
