from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

from src.database.base_class import Base

class Phone(Base):
    __tablename__ = "phones"

    id: Mapped[int] = mapped_column(primary_key=True)
    organization_id: Mapped[int] = mapped_column(ForeignKey("organizations.id"))
    phone_number: Mapped[str] = mapped_column(String(20), nullable=False)
    phone_type: Mapped[str] = mapped_column(String(15), nullable=False)

    organization = relationship("Organization", back_populates="phones")