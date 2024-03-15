#!/usr/bin/python3
"""contains the class definition of a City"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """Represents a city for a MySQL database.

    __tablename__ (str): The name of the MySQL table to store cities.
    id (sqlalchemy.Integer): The city's id.
    name (sqlalchemy.String): The city's name.
    state_id (sqlalchemy.Integer): The city's state id.
    state (relationship): Relationship to the State object.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship("State", back_populates="cities")
