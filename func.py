# func.py
from flask import Flask, request, render_template
import psycopg2

app = Flask(__name__)

def get_db_connection():
    # Read database settings from files
    with open('/bindings/db/database') as f:
        database = f.read().strip()
    with open('/bindings/db/host') as f:
        host = f.read().strip()
    with open('/bindings/db/password') as f:
        password = f.read().strip()
    with open('/bindings/db/port') as f:
        port = f.read().strip()
    with open('/bindings/db/provider') as f:
        provider = f.read().strip()
    with open('/bindings/db/type') as f:
        type_ = f.read().strip()
    with open('/bindings/db/username') as f:
        username = f.read().strip()

    # Build connection string
    conn_str = f"dbname={database} user={username} password={password} host={host} port={port}"

    # Connect to the database
    conn = psycopg2.connect(conn_str)

    return conn

def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create a simple table if it doesn't exist
    cursor.execute("CREATE TABLE IF NOT EXISTS values (id serial PRIMARY KEY, value varchar);")

    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def main():
    create_table()
    
    if request.method == 'POST':
        value = request.form['value']
        conn = get_db_connection()
        cursor = conn.cursor()

        # Insert the value into the database
        cursor.execute("INSERT INTO values (value) VALUES (%s);", (value,))

        conn.commit()
        conn.close()

    conn = get_db_connection()
    cursor = conn.cursor()

    # Retrieve values from the database
    cursor.execute("SELECT * FROM values;")
    values = cursor.fetchall()

    conn.close()

    return render_template('index.html', values=values)

if __name__ == '__main__':
    app.run(debug=True)
