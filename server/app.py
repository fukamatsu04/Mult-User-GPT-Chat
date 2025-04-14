from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
from auth.routes import auth_blueprint
from chat.sockets import socketio_events
from db.mongo import init_db
import os

app = Flask(__name__)
app.config.from_pyfile("config.py")
CORS(app, supports_credentials=True)

socketio = SocketIO(app, cors_allowed_origins="*")

# Register Blueprints
app.register_blueprint(auth_blueprint)

# Initialize DB
init_db()

# Register socket events
socketio_events(socketio)

@app.route("/")
def index():
    return {"message": "Backend is running!"}

if __name__ == "__main__":
    socketio.run(app, debug=True)