from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

# Base model for SQLAlchemy
Base = declarative_base()


# Define database model for MindCheck
class MindCheckRefined(Base):
    __tablename__ = "mind_checks"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    # PANAS ratings
    interested = Column(Integer, nullable=False)
    distressed = Column(Integer, nullable=False)
    excited = Column(Integer, nullable=False)
    upset = Column(Integer, nullable=False)
    strong = Column(Integer, nullable=False)
    guilty = Column(Integer, nullable=False)
    scared = Column(Integer, nullable=False)
    hostile = Column(Integer, nullable=False)
    enthusiastic = Column(Integer, nullable=False)
    proud = Column(Integer, nullable=False)
    irritable = Column(Integer, nullable=False)
    alert = Column(Integer, nullable=False)
    ashamed = Column(Integer, nullable=False)
    inspired = Column(Integer, nullable=False)
    nervous = Column(Integer, nullable=False)
    determined = Column(Integer, nullable=False)
    attentive = Column(Integer, nullable=False)
    jittery = Column(Integer, nullable=False)
    active = Column(Integer, nullable=False)
    afraid = Column(Integer, nullable=False)

    # Free text fields
    best_thing = Column(String(500), nullable=False)
    worst_thing = Column(String(500), nullable=False)

    # Demographic information
    location = Column(String, nullable=False)
    race_ethnicity = Column(String, nullable=False)
    gender_identity = Column(String, nullable=False)
