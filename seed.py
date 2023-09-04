# Import necessary modules and models from SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from models import Base, Restaurant, Customer, Review


# Define the database URL using sqlite
DATABASE_URL = "sqlite:///my_database.db"

# Create an SQLAlchemy engine to connect to the database
engine = create_engine(DATABASE_URL)

# Create the database tables based on the models defined in models.py
Base.metadata.create_all(engine)

# Create an SQLAlchemy session for interacting with the database
Session = sessionmaker(bind=engine)
session = Session()