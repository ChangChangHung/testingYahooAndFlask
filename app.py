from flask import Flask, render_template, jsonify, request
import os
import socket

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list_dir', methods=['GET'])
def list_dir():
    # 取得查詢目錄
    path = request.args.get('path', 'C:\\')  # 預設從 C 槽開始
    try:
        entries = []
        with os.scandir(path) as it:
            for entry in it:
                entries.append({
                    "name": entry.name,
                    "is_dir": entry.is_dir(),
                    "path": entry.path
                })
        return jsonify({"path": path, "entries": entries})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"\n✅ 手機請連到：http://{local_ip}:5000\n")
    app.run(host='0.0.0.0', port=5000, debug=True)
