User Authentication Flask Application Documentation

Overview: 
This Flask application provides a simple user authentication system where users can log in with their username and password. It uses a PostgreSQL database to store user information and provides an API endpoint for user authentication.

File Structure:

-- app.py: Contains the Flask application code.

-- login.html: HTML template for the login page.

-- style.css: CSS stylesheet for styling the login page.

-- wsgi.py: Contains the WSGI server code to run the Flask application.

-- vercel.json: Configuration file for Vercel deployment.

-- requirements.txt: List of Python dependencies.

-- index.py: Entry point for the Vercel deployment.

Dependencies:

-- Flask: A lightweight WSGI web application framework.

-- Psycopg2: A PostgreSQL adapter for Python.

Setup:

-- Clone the repository containing the Flask application code, html and css code.

-- Install dependencies

-- Set up a PostgreSQL database on Supabase and note down the connection details 

-- Push your code to a Git repository on GitHub

-- Configure the deployment settings in vercel.json to point to the correct entry point (index.py). Deploy your application on Vercel.

Usage:

-- Open the login page in your web browser. Enter your username and password. Click the "Sign In" button. If the authentication is successful, the application will display user data in JSON format.

API Endpoints:

-- GET /: Renders the login page.

-- POST /: Authenticates the user based on the provided username and password.

Test URL: https://ocs-sol.vercel.app


