from flask import Flask, render_template, request, jsonify
import hashlib
import psycopg2
import os



app = Flask(__name__)

# PostgreSQL connection parameters
db_params = {
    'dbname': 'postgres',
    'user': 'postgres.fcsxdnordedckinhrmyl',
    'password': os.getenv('DB_PASSWORD'),
    'host': 'aws-0-ap-south-1.pooler.supabase.com',
    'port': 5432,
}


# Function to hash passwords
def hash_password(raw_password):
    return hashlib.md5(raw_password.encode()).hexdigest()


# API endpoint for user authentication
@app.route('/', methods=['GET', 'POST'])
def authenticate_user():
    try:
        if request.method == 'GET':
            return render_template('login.html')

        elif request.method == 'POST':
            userid = request.form['userid']
            raw_password = request.form['password']
            password_hash = hash_password(raw_password)

            # Connect to the PostgreSQL database
            conn = psycopg2.connect(**db_params)
            cursor = conn.cursor()

            # Fetch user details from the database
            cursor.execute("SELECT * FROM public.users WHERE userid = %s AND password_hash = %s", (userid, password_hash))
            user_data = cursor.fetchone()

            if user_data:
                if user_data[2] == 'admin':
                    cursor.execute("SELECT * FROM public.users")
                    result = cursor.fetchall()
                else:
                    result = [user_data]

                    # Close database connection
                cursor.close()
                conn.close()

                return jsonify(result)

                    # Close database connection
            cursor.close()
            conn.close()

            return jsonify({'error': 'Authentication failed. Invalid credentials.'}), 401

    except Exception as e:
        return jsonify({'error': str(e)}), 500




