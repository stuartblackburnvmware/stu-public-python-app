from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def main():
    return "This is the greatest PUBLIC Python app ever written. Trust me."

@app.route('/api2')
def url2():
    return "This is the 2nd api endpoint"

@app.route('/api3')
def url3():
    return "This is the 3rd api endpoint"

if __name__ == '__main__':
    app.run(debug=True)
