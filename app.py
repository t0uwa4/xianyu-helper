from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "running",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

@app.route('/api/check', methods=['POST'])
def check_item():
    data = request.get_json()
    # 这里添加你的闲鱼商品检查逻辑
    return jsonify({
        "status": "success",
        "message": "检查完成"
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
