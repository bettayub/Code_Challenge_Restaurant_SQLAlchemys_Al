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


# Define data for creating customers and restaurants
customers_data = [("Mike", "Johnson"), ("Denno", "Smith"), ("Timothy", "Brown")]
restaurants_data = ["Quiver", "Villarosa", "Hilton"]

# Create Customer and Restaurant instances using list comprehensions
customers = [Customer(given_name=first_name, family_name=last_name) for first_name, last_name in customers_data]
restaurants = [Restaurant(name=name) for name in restaurants_data]

# Add all Customer and Restaurant instances to the session
session.add_all(customers + restaurants)

# Commit the changes to the database
session.commit()


# Define data for creating reviews and ratings
reviews_data = [
    (customers[0], restaurants[0], 4.5),
    (customers[1], restaurants[1], 3.8),
    (customers[2], restaurants[2], 4.0),
]

# Create Review instances using list comprehensions
reviews = [Review(customer=customer, restaurant=restaurant, rating_value=rating) for customer, restaurant, rating in reviews_data]

# Add all Review instances to the session
session.add_all(reviews)

# Commit the changes to the database
session.commit()
