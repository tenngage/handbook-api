from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text
from geoalchemy2 import Geometry

from src.database.base_class import Base

from src.models import Organization

class Building(Base):
    __tablename__ = "buildings"

    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[Text] = mapped_column(nullable=False)
    location: Mapped[Geometry] = mapped_column(Geometry(
        geometry_type="POINT",
        srid=4326,
    ))
    
    organization: Mapped["Organization"] = relationship(back_populates="building")