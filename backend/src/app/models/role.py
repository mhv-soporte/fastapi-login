import uuid
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    users = relationship("User", secondary="user_roles", back_populates="roles")
    permissions = relationship("Permission", secondary="role_permissions", back_populates="roles")
