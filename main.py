from contextlib import asynccontextmanager
from fastapi import FastAPI
from core import settings, db_helper
from presentation.api_v1.routers import api_v1_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_helper.engine.dispose()


app = FastAPI(lifespan=lifespan)


app.include_router(api_v1_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app="main:app",
        reload=settings.setup.reload,
        host=settings.setup.host,
        port=settings.setup.port,
    )
