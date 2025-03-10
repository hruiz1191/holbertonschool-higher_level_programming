#!/usr/bin/python3
"""First state model"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base  # Ahora solo importamos Base, sin `State`

class City(Base):
    """Base class for the cities table"""
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    # Relación con State
    state = relationship("State", back_populates="cities")

