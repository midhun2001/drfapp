1.  Create a database called drfapp in postgresql.

2.  Execute the following query for creating users table:

    CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    role VARCHAR(255) DEFAULT 'admin',
    username VARCHAR(255) UNIQUE,
    password VARCHAR(255)
    );

3.  Execute the following query for creating the association table:

    CREATE TABLE association (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    info VARCHAR(255),
    membership_fees DECIMAL,
    address VARCHAR(255),
    latitude DECIMAL,
    longitude DECIMAL,
    admin INTEGER REFERENCES users(id)
    );

4.  Install following requirements:

    pip install django djangorestframework

5.  Run the app

    python manage.py runserver

6.  Urls:

        -URLS- 			        -REQUESTS-

    /api/users/ : GET, POST
    /api/associations/ : GET, POST

7.  Post request fields:

    /users/ : [username, password]
    /associations/ : [name, info, membership_fees, latitude, longitude, admin]
