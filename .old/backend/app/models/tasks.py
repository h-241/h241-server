from app.models.service_provider import ServiceProvider
from sqlmodel import Field, Relationship, SQLModel


class Worker(BaseModel):
    name: str
    bio: str
    executions: list[Task]
    
    recovery_email: str
    icp_ledger_account_id: str
    
    min_task_duration: int
    min_task_price: int

class TaskRequest(BaseModel):
    description: str
    
    match_expiration_duration: int
    completion_expiration_duration: int
    
    max_price: int
    min_price: int
    
class Task(BaseModel):
    # we'll carbon copy this onto the chain
    
    task_request: TaskRequest
    task_provider: Worker
    start_time_ns: int
    end_time_ns: int
    
    amount_escrowed: int
    escrow_source: str
    amount_paid: int
    paid_to_icp_ledger_account_id: str
    
    duration: int

class Message(SQLModel):
    message: str