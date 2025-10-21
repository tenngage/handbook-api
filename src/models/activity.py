from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

from typing import Optional, List

from src.database.base_class import Base

class Activity(Base):
    __tablename__ = "activities"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    parent_id: Mapped[Optional[int]] = mapped_column(ForeignKey("activities.id"), nullable=True)

    parent: Mapped[Optional["Activity"]] = relationship(
        back_populates="children",
        remote_side=[id],
    )
    children: Mapped[List["Activity"]] = relationship(
        back_populates="parent",
    )