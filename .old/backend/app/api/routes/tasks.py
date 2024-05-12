from typing import Any

from fastapi import APIRouter, HTTPException
from sqlmodel import func, select

from app.api.deps import CurrentUser, SessionDep
from app.models.auth import Job, JobCreate, ItemPublic, ItemsPublic, JobUpdate, Message

router = APIRouter()


@router.get()
def create_task_request(*,
    session: SessionDep,
    current_user: CurrentUser,
    task_request_data: TaskRequest
    ) -> UUID4:
    ...

@router.get()
def get_available_task_requests(*,
    session: SessionDep,
    current_user: CurrentUser,
    task_provider_id: UUID4
    ) -> list[TaskRequest]:
    ...

@router.get()
def accept_task_request(*,
    session: SessionDep,
    current_user: CurrentUser,
    task_request_id: UUID4
    ) -> UUID4:
    ...

@router.get()
def add_message_to_task(*,
    session: SessionDep,
    current_user: CurrentUser,
    task_id: UUID4,
    message: str
    ):
    ...

@router.get()
def get_messages_for_task(*,
    session: SessionDep,
    current_user: CurrentUser,
    task_id: UUID4
    ) -> list[str]:
    ...

@router.get()
def cancel_task(*,
    session: SessionDep,
    current_user: CurrentUser,
    task_id: UUID4
    ):
    ...


