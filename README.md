# ecom_api
Simple API for a store
<h2> How to run </h2>

<h3>Step 1</h3>

Create a postgresql database and put these details into a `.env`:

`DEBUG=True`

`POSTGRES_DB=` the database name

`POSTGRES_USER=` database owner

`POSTGRES_PASSWORD=` database owner password

`POSTGRES_HOST=` default: localhost

`POSTGRES_PORT= `default: 5432

`SIGNING_KEY=  **KEY**` Signing key for JWT

<h3>Step 2</h3>

Create and activate a python venv and run:

`pip install -r ./requirements/base.txt`

<h3>Step 3</h3>

makemigrations and migrate the database

`python manage.py makemigrations`

`python manage.py migrate`

<h3>Step 4</h3>

Run the server using 

`python manage.py runserver`