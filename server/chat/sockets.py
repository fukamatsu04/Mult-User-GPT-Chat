from flask_socketio import SocketIO, emit
from db.mongo import messages_collection

socketio = SocketIO(cors_allowed_origins="*")

@socketio.on("connect")
def handle_connect():
    print("A user connected")

@socketio.on("message")
def handle_message(data):
    print("Received message:", data)
    messages_collection.insert_one({"text": data})
    emit("message", data, broadcast=True)
