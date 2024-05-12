from __future__ import annotations

from datetime import datetime
from typing import Literal
from pydantic import BaseModel, Field

class State(BaseModel):
    backend_start: datetime | None = None
    status: Literal['running', 'stopped'] = 'stopped'


state = State()

__all__ = ['state']
