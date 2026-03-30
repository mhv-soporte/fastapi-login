from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.session import get_db
from app.models.user import User
from app.core.hash import verify_password
from app.core.security import create_access_token
from app.schemas.auth import LoginRequest

router = APIRouter()

@router.post("/login")
async def login(data: LoginRequest, db: AsyncSession = Depends(get_db)):

    identifier = data.identifier or data.username

    if not identifier:
        raise HTTPException(status_code=400, detail="Falta usuario")

    result = await db.execute(
        select(User).where(
            (User.expediente == identifier) |
            (User.username == identifier)
        )
    )
    user = result.scalar_one_or_none()

    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Credenciales inválidas")

    token = create_access_token({"sub": user.expediente})

    return {"access_token": token, "token_type": "bearer"}
