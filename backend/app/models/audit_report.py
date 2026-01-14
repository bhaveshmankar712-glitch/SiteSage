import uuid
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.dialects.postgresql import JSONB, UUID

from app.db.base import Base

class AuditReport(Base):
    __tablename__ = "audit_reports"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    url = Column(String, nullable=False)

    seo_score = Column(Integer, nullable=False)
    issues = Column(JSONB, nullable=False)
    metrics = Column(JSONB, nullable=False)

    ai_summary = Column(String, nullable=True)
    ai_recommendations = Column(JSONB, nullable=True)

    created_at = Column(DateTime, default=datetime.now, nullable=False)
