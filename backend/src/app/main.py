from fastapi import FastAPI, Depends
from app.api.auth import router as auth_router
from app.api.deps import get_current_user
from app.db.session import engine
from app.db.base import Base
import app.db.models

from app.db.seed import seed_data
from sqlalchemy.ext.asyncio import async_sessionmaker

def create_app() -> FastAPI:
    app = FastAPI(title="Mi app")

    @app.on_event("startup")
    async def on_startup():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        from app.db.session import AsyncSessionLocal
        async with AsyncSessionLocal() as session:
            await seed_data(session)

    @app.get("/me")
    async def me(user = Depends(get_current_user)):
        return {
            "expediente": user.expediente,
            "username": user.username
        }

    app.include_router(auth_router, prefix="/auth")

    return app

app = create_app()
