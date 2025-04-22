from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
from auth.routes import auth_blueprint
from chat.sockets import socketio_events
from db.mongo import init_db, close_db
from config import Config  # Import Config class to load settings

app = Flask(__name__)
app.config.from_object(Config)
CORS(app, supports_credentials=True)

socketio = SocketIO(app, cors_allowed_origins="*")

# Register Blueprints
app.register_blueprint(auth_blueprint)

# Register socket events
socketio_events(socketio)

# Teardown DB connections
app.teardown_appcontext(close_db)

@app.route("/")
def index():
    return jsonify({"message": "Backend is running!"})

if __name__ == "__main__":
    with app.app_context():  # Set up the application context
        init_db()  # Initialize the database within the context
    socketio.run(app, debug=True)