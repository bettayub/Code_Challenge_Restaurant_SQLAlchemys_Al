# Import necessary modules and models from SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from models import Base, Restaurant, Customer, Review