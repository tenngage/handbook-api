from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

from typing import List

from src.database.base_class import Base

from src.models import Building, Phone

class Organization(Base):
    __tablename__ = "organizations"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    building_id: Mapped[int] = mapped_column(ForeignKey("buildings.id"), unique=True)

    building: Mapped["Building"] = relationship(back_populates="organization")
    phones: Mapped[List["Phone"]] = relationship(back_populates="organization")