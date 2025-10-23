from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

from typing import List

from src.database.base_class import Base

class Organization(Base):
    __tablename__ = "organizations"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    building_id: Mapped[int] = mapped_column(ForeignKey("buildings.id"), unique=True)

    building = relationship("Building", back_populates="organization")
    phones = relationship("Phone", back_populates="organization")