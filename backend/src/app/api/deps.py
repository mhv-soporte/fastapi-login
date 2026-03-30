from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from typing import Callable

from app.db.session import get_db
from app.models.user import User
from app.core.security import SECRET_KEY, ALGORITHM

security = HTTPBearer()

async def get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(security),
        db: AsyncSession = Depends(get_db)
):
    token = credentials.credentials
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        expediente: str = payload.get("sub")

        if expediente is None:
            raise HTTPException(status_code=401, detail='Token invalido')
    except JWTError:
        raise HTTPException(status_code=401, detail="Token invalido")
    
    result = await db.execute(
        select(User)
        .options(selectinload(User.roles))  # clave
        .where(User.expediente == payload["sub"])
    )

    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")
    
    return user

def require_role(role_name: str) -> Callable:
    async def role_checker(user: User = Depends(get_current_user)):
        user_roles = [role.name for role in user.roles]

        if role_name not in user_roles:
            raise HTTPException(
                status_code = status.HTTP_403_FORBIDDEN,
                detail="No tienes permisos suficientes",
            )
        return user
    
    return role_checker
