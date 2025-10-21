from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from src.database.base_class import Base

class OrganizationActivities(Base):
    __tablename__ = "organization_activities"

    organization_id: Mapped[int] = mapped_column(
        ForeignKey("organizations.id"),
        primary_key=True,
    )
    activity_id: Mapped[int] = mapped_column(
        ForeignKey("activities.id"),
        primary_key=True,
    )