from pydantic import BaseModel, Field


class BatchItem(BaseModel):
    """Pydantic model for representing a batch of numbers."""
    numbers: 'list[list[int]]'


class RequestModel(BaseModel):
    """Pydantic model for the request data."""
    batchid: str
    payload: 'list[BatchItem]'
