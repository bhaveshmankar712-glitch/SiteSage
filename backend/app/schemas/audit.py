from pydantic import BaseModel
from typing import List, Dict, Optional
from uuid import UUID
from datetime import datetime


class AuditCreateRequest(BaseModel):
    url: str


class AuditResponse(BaseModel):
    id: UUID
    url: str
    seo_score: int
    issues: List[str]
    metrics: Dict
    ai_summary: Optional[str]
    ai_recommendations: Optional[List[str]]
    created_at: datetime

    class Config:
        from_attributes = True


class AuditListItem(BaseModel):
    id: UUID
    url: str
    seo_score: int
    issues: List[str]
    metrics: Dict
    created_at: datetime

    class Config:
        from_attributes = True
