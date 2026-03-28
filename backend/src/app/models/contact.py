import uuid
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

class Contact(Base):
    __tablename__ = "contacts"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    organization: Mapped[str | None] = mapped_column(String, nullable=True)
    is_actibve: Mapped[bool] = mapped_column(Boolean, default=True)
