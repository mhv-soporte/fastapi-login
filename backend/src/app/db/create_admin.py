import asyncio
import app.db.models
from sqlalchemy.ext.asyncio import async_sessionmaker
from app.db.session import engine
from app.models.user import User
from app.core.hash import hash_password

AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

async def create_admin():
    async with AsyncSessionLocal() as session:
        user = User(
            expediente="admin001",
            username="adminuser",
            email=None,
            hashed_password=hash_password("admin123"),
            is_active=True,
            employee_type="confianza",
            position="gerente"
        )

        session.add(user)
        await session.commit()

if __name__ == "__main__":
    asyncio.run(create_admin())