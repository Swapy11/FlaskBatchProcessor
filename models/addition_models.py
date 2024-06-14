# models/addition_models.py
from typing import List
from pydantic import BaseModel


class AdditionRequest(BaseModel):
    """
    Pydantic model for representing addition request data.
    """
    batchid: str
    payload: List[List[int]]


class AdditionResponse(BaseModel):
    """
    Pydantic model for representing addition response data.
    """
    batchid: str
    response: List[int]
    status: str
    started_at: str
    completed_at: str
