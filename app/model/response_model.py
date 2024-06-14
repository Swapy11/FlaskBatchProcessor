from pydantic import BaseModel, Field
from datetime import datetime


class ResponseItem(BaseModel):
    """Pydantic model for representing a response item."""
    result: int


class ResponseModel(BaseModel):
    """Pydantic model for the response data."""
    batchid: str
    response: 'list[ResponseItem]' = []
    status: str = "incomplete"
    started_at: datetime = Field(default_factory=datetime.now(datetime.UTC))
    completed_at: datetime = Field(default_factory=datetime.now(datetime.UTC))
