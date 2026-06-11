import { useState } from "react";
import axios from "axios";

function ChatPanel({ messages, setMessages }) {
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = {
      sender: "user",
      text: input,
    };

    setMessages((prev) => [...prev, userMessage]);

    const currentInput = input;
    setInput("");

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/assistant",
        {
          message: currentInput,
        }
      );

      const assistantMessage = {
        sender: "assistant",
        text:
          response.data.message ||
          JSON.stringify(response.data),
      };

      setMessages((prev) => [
        ...prev,
        assistantMessage,
      ]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          sender: "assistant",
          text:
            "⚠️ Unable to connect to backend.",
        },
      ]);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      sendMessage();
    }
  };

  return (
    <div className="flex flex-col h-screen">

      {/* Header */}
      <div className="p-8 border-b border-slate-800">
        <h1 className="text-5xl font-bold">
          VIDUR
        </h1>

        <p className="text-slate-400 mt-2">
          Intelligent Personal Assistant
        </p>
      </div>

      {/* Messages */}
      <div className="flex-1 overflow-y-auto p-8">

        <div className="space-y-6">

          {messages.map((msg, index) => (
            <div
              key={index}
              className={`flex ${
                msg.sender === "user"
                  ? "justify-end"
                  : "justify-start"
              }`}
            >
              <div
                className={`max-w-[70%] p-4 rounded-2xl ${
                  msg.sender === "user"
                    ? "bg-blue-600 text-white"
                    : "bg-[#131827] text-white"
                }`}
              >
                {msg.text}
              </div>
            </div>
          ))}

        </div>

      </div>

      {/* Input */}
      <div className="p-6 border-t border-slate-800">

        <div className="flex gap-4">

          <input
            type="text"
            placeholder="Type your message..."
            value={input}
            onChange={(e) =>
              setInput(e.target.value)
            }
            onKeyDown={handleKeyDown}
            className="
              flex-1
              bg-[#131827]
              text-white
              rounded-xl
              px-4
              py-3
              outline-none
            "
          />

          <button
            onClick={sendMessage}
            className="
              bg-blue-600
              hover:bg-blue-700
              px-6
              rounded-xl
            "
          >
            Send
          </button>

        </div>

      </div>

    </div>
  );
}

export default ChatPanel;