from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample in-memory data
attendance = {}

@app.route('/')
def home():
    return "Welcome to the Student Attendance Tracker!"

@app.route('/mark', methods=['POST'])
def mark_attendance():
    data = request.json
    name = data.get('name')
    status = data.get('status', 'present')

    if name:
        attendance[name] = status
        return jsonify({"message": f"{name} marked as {status}"}), 200
    return jsonify({"error": "Name required"}), 400

@app.route('/list', methods=['GET'])
def list_attendance():
    return jsonify(attendance)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
