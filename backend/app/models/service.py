from app.models.service_provider import ServiceProvider
from sqlmodel import Field, Relationship, SQLModel


class ServiceOfferringBase(SQLModel):
    title: str
    description: str | None = None
    price: float
    duration: int
    service_provider_id: int | None = Field(default=None, foreign_key="serviceprovider.id", nullable=False)
    service_provider: ServiceProvider | None = Relationship(back_populates="services_offered")

