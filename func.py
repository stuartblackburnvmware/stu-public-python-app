# func.py
from flask import Flask, request, render_template
import psycopg2

app = Flask(__name__)

def get_db_connection():
    # ... (same as before)

def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    # ... (same as before)

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
