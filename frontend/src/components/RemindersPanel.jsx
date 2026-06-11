import { useEffect, useState } from "react";
import axios from "axios";

function RemindersPanel() {
  const [reminders, setReminders] = useState([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/reminders")
      .then((res) => setReminders(res.data))
      .catch((err) => console.log(err));
  }, []);

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-6">
        Reminders
      </h1>

      <div className="space-y-4">
        {reminders.map((reminder) => (
          <div
            key={reminder.id}
            className="bg-[#131827] p-4 rounded-xl"
          >
            <div>{reminder.title}</div>
            <div className="text-slate-400 text-sm">
              {reminder.remind_at}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default RemindersPanel;