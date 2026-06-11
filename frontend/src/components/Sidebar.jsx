import {
  MessageSquare,
  CheckSquare,
  Target,
  Bell,
} from "lucide-react";

function Sidebar({ setView }) {
  return (
    <div className="w-64 bg-[#0b1020] border-r border-slate-800 h-screen">

      <div className="p-6">
        <h1 className="text-3xl font-bold">
          VIDUR
        </h1>

        <p className="text-slate-400 text-sm mt-1">
          Personal Assistant
        </p>
      </div>

      <div className="flex flex-col gap-2 p-4">

        <button
          onClick={() => setView("chat")}
          className="flex items-center gap-3 p-3 rounded-xl hover:bg-slate-800"
        >
          <MessageSquare size={20}/>
          Chat
        </button>

        <button
          onClick={() => setView("tasks")}
          className="flex items-center gap-3 p-3 rounded-xl hover:bg-slate-800"
        >
          <CheckSquare size={20}/>
          Tasks
        </button>

        <button
          onClick={() => setView("goals")}
          className="flex items-center gap-3 p-3 rounded-xl hover:bg-slate-800"
        >
          <Target size={20}/>
          Goals
        </button>

        <button
          onClick={() => setView("reminders")}
          className="flex items-center gap-3 p-3 rounded-xl hover:bg-slate-800"
        >
          <Bell size={20}/>
          Reminders
        </button>

      </div>

    </div>
  );
}

export default Sidebar;