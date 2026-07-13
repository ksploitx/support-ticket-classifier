from pydantic import BaseModel
from typing import Optional

class TicketRequest(BaseModel):
    text: str

class TicketResponse(BaseModel):
    category: str
    confidence: Optional[float] = None
    method: str
