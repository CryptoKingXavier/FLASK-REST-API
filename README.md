# FLASK-REST-API

##### CREATING A REST API (V1.0) USING PYTHON, FLASK (WEB FRAMEWORK), SQLAlchemy (OBJECT RELATIONAL MAPPING DATABASE), Marshmallow (SERIALIZATION/DESERIALIZATION FRAMEWORK)

To create a REST API in Flask using SQLAlchemy and Marshmallow, you will need to perform the following steps:

Set up a Flask project: Start by setting up a new Flask project and creating a basic API structure. You will need to install Flask, SQLAlchemy, and Marshmallow using pip.

Create a database model: Define a model class for the object that you want to store in the database, using SQLAlchemy's ORM. This model should define the fields and data types of the object, as well as any relationships with other objects.

Create a schema: Define a Marshmallow schema class for the object, which will be used to serialize and deserialize the object when working with the API. The schema should define the fields of the object and any additional metadata, such as data validation rules.

Set up the database: Initialize the database and create any necessary tables. You can do this using SQLAlchemy's create_all() method.

Define API routes: Define the routes for your API, using Flask's @app.route decorator. Each route should correspond to a specific HTTP method (e.g. GET, POST, PUT, DELETE) and should specify the actions to take when that method is called.

Write API logic: Write the logic for each of your API routes, using the methods provided by SQLAlchemy and Marshmallow to query the database and serialize/deserialize objects.

Test the API: Test your API using a tool like Postman to ensure that it is working as expected.
