import uuid
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)

    expediente: Mapped[str] = mapped_column(String, unique=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)

    email: Mapped[str | None] = mapped_column(String, nullable=True)
    
    hashed_password: Mapped[str] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    employee_type: Mapped[str] = mapped_column(String) # Sindicalizado | confianza

    area_id: Mapped[uuid.UUID] = mapped_column(nullable=True)

    grade: Mapped[str | None] = mapped_column(String, nullable=True)
    position: Mapped[str | None] = mapped_column(String, nullable=True)

    area_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("areas.id"), nullable=True)

    area = relationship("Area", back_populates="users")
    roles = relationship("Role", secondary="user_roles", back_populates="users")
