from sqlmodel import Field, Relationship, SQLModel



# JSON payload containing access token
class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"


# Contents of JWT token
class TokenPayload(SQLModel):
    sub: int | None = None


class NewPassword(SQLModel):
    token: str
    new_password: str

from app.models.user import User
from sqlmodel import Field, Relationship, SQLModel


# Shared properties
class JobBase(SQLModel):
    title: str
    description: str | None = None


# Properties to receive on item creation
class JobCreate(JobBase):
    title: str


# Properties to receive on item update
class JobUpdate(JobBase):
    title: str | None = None  # type: ignore


# Database model, database table inferred from class name
class Job(JobBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    owner_id: int | None = Field(default=None, foreign_key="user.id", nullable=False)
    owner: User | None = Relationship(back_populates="items")


# Properties to return via API, id is always required
class ItemPublic(JobBase):
    id: int
    owner_id: int


class ItemsPublic(SQLModel):
    data: list[ItemPublic]
    count: int
    
from sqlmodel import Field, Relationship, SQLModel


# Generic message
class Message(SQLModel):
    message: str
    
from app.models.service import ServiceOfferringBase
from sqlmodel import Field, Relationship, SQLModel
from app.models.user import User

# Subclassing User to create a ServiceProvider model
class ServiceProvider(User, table=True):
    # Additional fields specific to a ServiceProvider
    services_offered: list[ServiceOfferringBase] = Relationship(back_populates="service_provider")
    availability: str = Field(default=None)
    rating: float = Field(default=None, index=True)

from app.models.service_provider import ServiceProvider
from sqlmodel import Field, Relationship, SQLModel


class ServiceOfferringBase(SQLModel):
    title: str
    description: str | None = None
    price: float
    duration: int
    service_provider_id: int | None = Field(default=None, foreign_key="serviceprovider.id", nullable=False)
    service_provider: ServiceProvider | None = Relationship(back_populates="services_offered")


# Shared properties
# TODO replace email str with EmailStr when sqlmodel supports it
from sqlmodel import Field, Relationship, SQLModel


class UserBase(SQLModel):
    email: str = Field(unique=True, index=True)
    is_active: bool = True
    is_superuser: bool = False
    full_name: str | None = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str


# TODO replace email str with EmailStr when sqlmodel supports it
class UserRegister(SQLModel):
    email: str
    password: str
    full_name: str | None = None


# Properties to receive via API on update, all are optional
# TODO replace email str with EmailStr when sqlmodel supports it
class UserUpdate(UserBase):
    email: str | None = None  # type: ignore
    password: str | None = None


# TODO replace email str with EmailStr when sqlmodel supports it
class UserUpdateMe(SQLModel):
    full_name: str | None = None
    email: str | None = None


class UpdatePassword(SQLModel):
    current_password: str
    new_password: str


# Database model, database table inferred from class name
class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str
    items: list["Job"] = Relationship(back_populates="owner")


# Properties to return via API, id is always required
class UserPublic(UserBase):
    id: int


class UsersPublic(SQLModel):
    data: list[UserPublic]
    count: int

##  TODO: use couchbase for the db in the backend