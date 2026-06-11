import { useEffect, useState } from "react";
import axios from "axios";

function GoalsPanel() {
  const [goals, setGoals] = useState([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/memory")
      .then((res) => setGoals(res.data))
      .catch((err) => console.log(err));
  }, []);

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-6">
        Goals & Memory
      </h1>

      <div className="space-y-4">
        {goals.map((item) => (
          <div
            key={item.id}
            className="bg-[#131827] p-4 rounded-xl"
          >
            <strong>{item.key}</strong>: {item.value}
          </div>
        ))}
      </div>
    </div>
  );
}

export default GoalsPanel;