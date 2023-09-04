# Import necessary modules from SQLAlchemy
# Create the SQLAlchemy engine to connect to the database
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


# Define the base class for declarative models
Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    # Defining columns for the table
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    price = Column(Integer)


    reviews = relationship('Review', back_populates='restaurant')
    customers = relationship('Customer', secondary='reviews')

# Define the Customer model
class Customer(Base):
    # Specify the name of the table
    __tablename__ = 'customers'

    # Define columns for the table
    id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))


    reviews = relationship('Review', back_populates='customer')

    restaurants = relationship('Restaurant', secondary='reviews')

# Define the Review model
class Review(Base):
    # Specify the name of the table
    __tablename__ = 'reviews'

    # Define columns for the table
    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'), nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)

    # Define the relationships with Restaurant and Customer models
    restaurant = relationship('Restaurant', back_populates='reviews')
    customer = relationship('Customer', back_populates='reviews')


