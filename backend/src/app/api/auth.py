from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.session import get_db
from app.models.user import User
from app.core.hash import verify_password
from app.core.security import create_access_token

router = APIRouter()

@router.post("/login")
async def login(data: dict, db: AsyncSession = Depends(get_db)):
    identifier = data.get("identifier")
    password = data.get("password")

    result = await db.execute(
        select(User).where(
            (User.expediente == identifier) |
            (User.username == identifier)
        )
    )
    user = result.scalar_one_or_none()

    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Credenciales inválidas")

    token = create_access_token({"sub": user.expediente})

    return {"access_token": token, "token_type": "bearer"}
