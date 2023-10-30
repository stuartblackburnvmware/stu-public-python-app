# func.py

from app import app  # Import the Flask app

def main(req):
    # Main application logic goes here
    # You can call the Flask app routes if needed, but don't run the app here

    if __name__ == '__main__':
        app.run(debug=True)
