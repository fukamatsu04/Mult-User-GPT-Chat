from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit

app = Flask(__name__)
CORS(app, supports_credentials=True)

socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def index():
    return jsonify({"message": "Backend is running!"})

@socketio.on("message")
def handle_message(data):
    print("Received message:", data)
    emit("message", data, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, debug=True)