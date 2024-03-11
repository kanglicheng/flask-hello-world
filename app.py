from flask import Flask
app = Flask(__name__)

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
