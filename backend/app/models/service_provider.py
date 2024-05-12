from app.models.service import ServiceOfferringBase
from sqlmodel import Field, Relationship, SQLModel
from app.models.user import User

# Subclassing User to create a ServiceProvider model
class ServiceProvider(User, table=True):
    # Additional fields specific to a ServiceProvider
    services_offered: list[ServiceOfferringBase] = Relationship(back_populates="service_provider")
    availability: str = Field(default=None)
    rating: float = Field(default=None, index=True)
