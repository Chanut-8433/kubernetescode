from flask import Flask, jsonify

# สร้าง Flask instance
app = Flask(__name__)

# Route หลัก
@app.route('/')
def home():
    return 'Linuxgray Training Center - 5'

# Route สำหรับ health check (ใช้กับ Docker/K8s ได้ดี)
@app.route('/health')
def health():
    return jsonify(status="UP"), 200

# รันเซิร์ฟเวอร์
if __name__ == '__main__':
    # host=0.0.0.0 เปิดให้ container/network ภายนอกเข้าถึงได้
    app.run(host='0.0.0.0', port=5000, debug=True)
