# Import necessary modules from SQLAlchemy
# Create the SQLAlchemy engine to connect to the database
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Define the base class for declarative models
Base = declarative_base()

# Define the Customer model
class Customer(Base):
    __tablename__ = "customers"

    # Defining columns for the table
    id = Column(Integer, primary_key=True)
    given_name = Column(String)
    family_name = Column(String)

    # Define a bidirectional relationship between Customer and Review models
    reviews = relationship("Review", back_populates="customer")

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    def favorite_restaurant(self):
        favorite_review = max(self.reviews, key=lambda review: review.rating_value, default=None)
        return favorite_review.restaurant if favorite_review else None

    # This method allows a customer to add a new review with a specified restaurant and rating.
    # createing a new Review instance, associates it with the customer and restaurant, and saves it to the database.
    def add_review(self, restaurant, rating):
        new_review = Review(customer=self, restaurant=restaurant, rating=rating)
        session.add(new_review)
        session.commit()


    # Deletes a customer's reviews for a specific restaurant from the database.
    def delete_reviews(self, restaurant):
        reviews_to_delete = [review for review in self.reviews if review.restaurant == restaurant]
        for review in reviews_to_delete:
            session.delete(review)
        session.commit()


     # Define the Restaurant model
class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    reviews = relationship("Review", back_populates="restaurant")

    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_ratings = sum(review.rating_value for review in self.reviews)
        return total_ratings / len(self.reviews)

    @classmethod
    def fanciest(cls):
        return session.query(cls).order_by(cls.price.desc()).first()

    def all_reviews(self):
        return [review.full_review() for review in self.reviews]

     
    # Define the Review model
class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    rating_value = Column(Float)

    customer_id = Column(Integer, ForeignKey("customers.id"))
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))

    customer = relationship("Customer", back_populates="reviews")
    restaurant = relationship("Restaurant", back_populates="reviews")

    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.rating_value} stars"
