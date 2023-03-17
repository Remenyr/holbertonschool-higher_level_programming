#!/usr/bin/python3
"""
Python file that contains the class definition of a City
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    City class that creates a table
    """
    __tablename__ = 'cities'

    id = Column(Integer(), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey(State.id), nullable=False)