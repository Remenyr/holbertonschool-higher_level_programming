#!/usr/bin/python3
"""
Script that changes the name of a State object from a database
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()

    louisiana = session.query(State).filter_by(id=2).first()
    louisiana.name = 'New Mexico'
    session.commit()