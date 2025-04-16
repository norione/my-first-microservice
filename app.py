from flask import Flask, jsonify
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

app = Flask(__name__)

# 配置
app.config['JSON_AS_ASCII'] = False  # 支持中文
app.config['JSON_SORT_KEYS'] = False  # 保持JSON键的顺序

@app.route('/')
def index():
    return jsonify({
        "message": "欢迎使用微服务",
        "endpoints": {
            "health": "/health",
            "hello": "/api/v1/hello"
        }
    })

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "version": "1.0.0",
        "environment": os.getenv('FLASK_ENV', 'production')
    })

@app.route('/api/v1/hello', methods=['GET'])
def hello():
    return jsonify({
        "message": "你好，这是微服务",
        "version": "1.0.0"
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV', 'production') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug) 