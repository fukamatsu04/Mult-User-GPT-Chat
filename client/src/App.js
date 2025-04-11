import React, { useEffect, useState } from "react";
import io from "socket.io-client";

const socket = io("http://localhost:5000"); // backend URL

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  useEffect(() => {
    socket.on("message", (msg) => {
      setMessages((prev) => [...prev, msg]);
    });
    return () => socket.off("message");
  }, []);

  const sendMessage = () => {
    if (input.trim()) {
      socket.emit("message", input);
      setInput("");
    }
  };

  return (
    <div className="flex flex-col h-screen justify-between p-4 bg-gray-100">
      <h1 className="text-3xl font-bold text-center text-blue-600 mb-4">Chat App</h1>
      
      <div className="flex-grow overflow-y-auto bg-white p-4 rounded-lg shadow-lg space-y-2">
        {messages.map((msg, i) => (
          <p key={i} className="text-gray-700 p-2 bg-blue-100 rounded-md">
            {msg}
          </p>
        ))}
      </div>
      
      <div className="flex items-center space-x-2 mt-4">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          className="flex-grow p-2 border rounded-lg border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
          placeholder="Type a message..."
        />
        <button
          onClick={sendMessage}
          className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
        >
          Send
        </button>
      </div>
    </div>
  );
}

export default App;

