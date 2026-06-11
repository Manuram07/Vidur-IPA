import { useEffect, useState } from "react";
import axios from "axios";

function TasksPanel() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/tasks")
      .then((res) => setTasks(res.data))
      .catch((err) => console.log(err));
  }, []);

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-6">
        Tasks
      </h1>

      <div className="space-y-4">
        {tasks.map((task) => (
          <div
            key={task.id}
            className="bg-[#131827] p-4 rounded-xl"
          >
            {task.title}
          </div>
        ))}
      </div>
    </div>
  );
}

export default TasksPanel;