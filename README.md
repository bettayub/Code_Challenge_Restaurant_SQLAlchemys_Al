# Code Challenge - SQLAlchemy Restaurant
## Author
BETT AYUB

## Description:
This project designs three models: Restaurant, Review, and Customer. In this setup, a Restaurant can have multiple Reviews, a Customer can leave multiple Reviews, and each Review is associated with both a Restaurant and a Customer. Specifically, the Restaurant-Customer relationship is a many-to-many connection. We'll utilize SQLAlchemy for this project, and we also have a seeds.py file to generate sample data for testing the models and their relationships.

Table of Contents
Introduction
Getting Started
Usage
Class Descriptions
Dependencies
Contributing
License

## Project Overview
In this project, we're focusing on three main components:

Customer Model: This part of our project represents individual customers who can contribute valuable reviews based on their experiences.

## Restaurant Model: 
The restaurant model encompasses essential details like the restaurant's name, price range, and its ability to both receive and provide reviews from customers.

Review Model: Reviews are written by customers to provide feedback and star ratings for specific restaurants. Each review is associated with both a customer and a restaurant, forming a network of feedback.

## Technologies Utilized
Python:
We utilize Python, a widely-used high-level programming language, known for its simplicity, readability, and versatility.

## SQLAlchemy:
SQLAlchemy serves as an essential technology in our project. It's an open-source Python library used for Object-Relational Mapping (ORM). SQLAlchemy offers a set of user-friendly tools for interacting with relational databases using Python code. The primary purpose of SQLAlchemy is to bridge the gap between the object-oriented Python programming language and relational database management systems (RDBMS), which store and manage data in a tabular format.

## Getting Started
To begin with our Toy Problem project, follow these steps:





Clone the repository to your local machine using the following command:

https://github.com/bettayub/Code_Challenge_Restaurant_SQLAlchemys_AlNavigate to the project directory:

cd Code_Challenge_Restaurant_SQLAlchemys_Al
Install the required dependencies:

pipenv --python 3.10 * pipenv install * pipenv shell * pip install SQLAlchemy
Usage
The project demonstrates how to establish relationships between classes, create instances, and use the provided methods for interacting with those instances.

Class Descriptions
Customer

Represents a customer. * Attributes: - given_name: The customer's given name. - family_name: The customer's family name. - reviews: A list of reviews written by the customer. * Methods: - get_given_name(): Get the customer's given name. - get_family_name(): Get the customer's family name. - full_name(): Get the full name of the customer. - add_review(review): Associate a review with this customer. - get_reviews(): Get all reviews associated with this customer.
Restaurant

Represents a restaurant. * Attributes: - restaurant_name: The name of the restaurant. - restaurant_reviews: A list of reviews received by the restaurant. * Methods: - get_name(): Get the restaurant's name. - add_review(review): Associate a review with this restaurant. - get_reviews(): Get all reviews associated with this restaurant. - get_customers(): Get all customers who reviewed this restaurant. - average_star_rating(): Calculate the average star rating of the restaurant.
Review

Represents a review. - Attributes: - customer: The customer who wrote the review. - restaurant: The restaurant being reviewed. - rating: The rating given in the review. * Methods: - get_rating(): Get the rating of the review. - get_customer(): Get the customer associated with the review. - get_restaurant(): Get the restaurant associated with the review.
Dependencies
Python 3.9 or higher is recommended for this program as it was developed in version 3.8 but should work on any newer
Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests

# License
MIT License

Copyright (c) 2023 BETT AYUB

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,