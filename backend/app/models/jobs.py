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