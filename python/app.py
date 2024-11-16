from flask import Flask, jsonify, send_from_directory
import requests
import pandas as pd
from datetime import datetime
import os

# Spring Boot API URL
SPRINGBOOT_API = 'http://userservice:8080/users'

# 엑셀 파일 저장 경로
EXPORT_PATH = '/app/export/'

app = Flask(__name__)

def fetch_users():
    """Spring Boot API에서 사용자 데이터를 가져옵니다."""
    try:
        response = requests.get(SPRINGBOOT_API)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

def export_to_excel(users):
    """사용자 데이터를 엑셀 파일로 내보냅니다."""
    try:
        # 데이터를 DataFrame으로 변환
        df = pd.DataFrame(users)
        if not df.empty:
            # 파일 이름에 현재 날짜/시간 추가
            filename = f"users_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
            file_path = os.path.join(EXPORT_PATH, filename)
            df.to_excel(file_path, index=False)
            print(f"Data exported to {file_path}")
            return filename
        else:
            print("No data to export.")
    except Exception as e:
        print(f"Error exporting to Excel: {e}")
        return None

@app.route('/export', methods=['GET'])
def export_data():
    """사용자 데이터를 엑셀로 내보내는 Flask 엔드포인트."""
    print("Fetching data from Spring Boot...")
    users = fetch_users()
    if users:
        print("Exporting data to Excel...")
        filename = export_to_excel(users)
        if filename:
            return jsonify({"message": "Export successful", "file": filename})
        else:
            return jsonify({"message": "Failed to export data"}), 500
    return jsonify({"message": "No data to export"}), 404

@app.route('/export/<filename>', methods=['GET'])
def export_file(filename):
    """엑셀 파일을 다운로드할 수 있게 처리."""
    try:
        # Flask의 send_from_directory를 사용해 파일을 제공
        return send_from_directory(EXPORT_PATH, filename)
    except FileNotFoundError:
        return jsonify({"message": "File not found"}), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
