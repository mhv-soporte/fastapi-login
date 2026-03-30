from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.area import Area
from app.models.role import Role
from app.models.permission import Permission

async def seed_data(session: AsyncSession):
    # Areas
    areas = ["Metro", "Nacional"]

    for name in areas:
        result = await session.execute(select(Area).where(Area.name == name))
        if not result.scalar():
            session.add(Area(name=name))

    # Roles
    roles = ["admin", "operador", "scraper", "anaista"]

    for role_name in roles:
        result = await session.execute(select(Role).where(Role.name == name))
        role = result.scalar_one_or_none
        if not role:
            session.add(Role(name=role_name))

    # Permisos
    permissions = [
        "view_calls",
        "create_calls",
        "run_scraping",
        "view_analytics",
        "manage_users",
    ]

    for name in permissions:
        result = await session.execute(select(Permission).where(Permission.name == name))
        if not result.scalar():
            session.add(Permission(name=name))

    await session.commit()
