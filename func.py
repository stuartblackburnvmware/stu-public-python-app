from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return "This is the greatest PUBLIC python app ever written. Trust me."

if __name__ == '__main__':
    app.run(debug=True)
