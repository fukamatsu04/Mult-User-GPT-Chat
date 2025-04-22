from flask_socketio import emit
from db.mongo import get_db  # Function to retrieve MongoDB connection from Flask's application context

def socketio_events(socketio):
    """
    Register all Socket.IO events with the given SocketIO instance.
    """

    @socketio.on("connect")
    def handle_connect():
        """
        Event handler for new client connections.
        When a client connects, fetch the last 20 messages from the database
        and send them back to the client as chat history.
        """
        print("Client connected")
        db = get_db()  # Get the current database connection
        recent_messages = db.messages.find().sort("_id", -1).limit(20)  # Fetch latest 20 messages
        # Format the messages for sending to the client
        history = [{"text": msg["text"]} for msg in recent_messages]
        # Emit the message history to the connected client (most recent message last)
        emit("history", history[::-1])

    @socketio.on("message")
    def handle_message(data):
        """
        Event handler for incoming chat messages.
        Saves the received message to the database and broadcasts it to all connected clients.
        """
        print("Received message:", data)
        db = get_db()  # Get the current database connection
        # Insert the new message into the 'messages' collection
        db.messages.insert_one({"text": data})
        # Broadcast the new message to all connected clients
        emit("message", data, broadcast=True)