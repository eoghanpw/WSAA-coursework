from flask import Flask, url_for, request, redirect, abort

app = Flask(__name__, static_url_path='', static_folder='staticpages')


# test
@app.route('/')
def index():
    return "hello"


# get all
@app.route('/stocks', methods=['GET'])
def get_all():
    return "get all"


# get by ticker
@app.route('/stocks/<ticker>', methods=['GET'])
def find_by_ticker(ticker):
    return "find by ticker"


# create
@app.route('/stocks', methods=['POST'])
def create():
    json_string = request.json
    return f"create {json_string}"


# update
@app.route('/stocks/<ticker>', methods=['PUT'])
def update(ticker):
    json_string = request.json
    return f"update {ticker} {json_string}"


# delete
@app.route('/stocks/<ticker>', methods=['DELETE'])
def delete(ticker):
    return f"delete {ticker}"


if __name__ == "__main__":
    app.run(debug=True)
