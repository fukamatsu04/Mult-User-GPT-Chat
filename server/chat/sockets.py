def socketio_events(socketio):
    @socketio.on("message")
    def handle_message(data):
        print("Received:", data)
        socketio.emit("message", data, broadcast=True)
