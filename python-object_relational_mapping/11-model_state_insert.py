#!/usr/bin/python3
"""Fetches states from dtatbase"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """create engine"""
    if len(sys.argv) != 4:
        print("wrong")
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    s1 = State(name="Louisiana")
    session.add(s1)
    session.commit()
    print(f"{s1.id}")
    session.close()
