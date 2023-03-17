#!/usr/bin/python3
"""
script that prints the State object with the name passed as argument
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

    state = session.query(State).filter(State.name == '%s' % argv[4]).first()

    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
