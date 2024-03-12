from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/stock/<ticker>')
def get_stock_data(ticker):
    if ticker == "AAPL":
        return jsonify({"name": "Apple Inc.", "last_price": 181.30, "ticker": "AAPL", "market_cap": "2.797T"})

    if ticker == "META":
        return jsonify({"name": "Meta Platforms, Inc.", "last_price": 481.74, "ticker": "META", "market_cap": "1.228T"})

    if ticker == "COIN":
        return jsonify({"name": "Coinbase Global, Inc.", "last_price": 193.94, "ticker": "COIN", "market_cap": "46.987B"})

    if ticker == "SMCI":
        return jsonify({"name": "Super Micro Computer, Inc.", "last_price": 895.93, "ticker": "SMCI", "market_cap": "46.987B"})
    if ticker == "NOW":
        return jsonify({"name": "Service Now Inc", "last_price": 732.66, "ticker": "NOW", "market_cap": "98B"})
