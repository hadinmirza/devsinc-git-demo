from flask import Flask, jsonify
from data_processor import normalize_features

app = Flask(__name__)

@app.route('/process')
def process():
    return jsonify({"output": normalize_features([12, 45, 67, 89, 34])})

if __name__ == '__main__':
    app.run()