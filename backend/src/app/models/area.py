import uuid
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

class Area(Base):
    __tablename__ = "areas"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4) 
    name: Mapped[str] = mapped_column(String, unique=True)

    users = relationship("User", back_populates="area")
