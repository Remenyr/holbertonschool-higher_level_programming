#!/usr/bin/python3
"""
Python file that contains the class definition of a State and
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    Creating a table
    """
    __tablename__ = 'states'
    id = Column(Integer(), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
