from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "message": "Welcome to Microservice",
        "endpoints": {
            "health": "/health",
            "hello": "/api/v1/hello"
        }
    })

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})

@app.route('/api/v1/hello', methods=['GET'])
def hello():
    return jsonify({
        "message": "Hello from Microservice",
        "version": "1.0.0"
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 