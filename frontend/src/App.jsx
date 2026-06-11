import { useState } from "react";

import Sidebar from "./components/Sidebar";
import ChatPanel from "./components/ChatPanel";
import TasksPanel from "./components/TasksPanel";
import GoalsPanel from "./components/GoalsPanel";
import RemindersPanel from "./components/RemindersPanel";

function App() {
  const [view, setView] = useState("chat");

  const [messages, setMessages] = useState([
    {
      sender: "assistant",
      text: "Hello Ram 👋",
    },
    {
      sender: "assistant",
      text: "How can I help you today?",
    },
  ]);

  return (
    <div className="flex bg-[#050816] text-white min-h-screen">
      <Sidebar setView={setView} />

      <div className="flex-1">
        {view === "chat" && (
          <ChatPanel
            messages={messages}
            setMessages={setMessages}
          />
        )}

        {view === "tasks" && (
          <TasksPanel />
        )}

        {view === "goals" && (
          <GoalsPanel />
        )}

        {view === "reminders" && (
          <RemindersPanel />
        )}
      </div>
    </div>
  );
}

export default App;