#!/usr/bin/python3
"""
Updates the name of the State object with id = 2 to 'New Mexico'
in the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create the database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the state with id = 2
    state = session.query(State).filter_by(id=2).first()

    if state:
        state.name = "New Mexico"  # Update the name
        session.commit()  # Save changes

    # Close session
    session.close()
