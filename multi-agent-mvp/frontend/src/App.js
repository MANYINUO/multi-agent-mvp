import React, { useState } from "react";
import { createTask } from "./api";

function App() {
  const [task, setTask] = useState("");
  const [result, setResult] = useState(null);

  const handleRun = async () => {
    const res = await createTask(task);
    setResult(res);
  };

  return (
    <div>
      <h1>Multi-Agent Automation MVP</h1>
      <input value={task} onChange={e => setTask(e.target.value)} placeholder="Task name"/>
      <button onClick={handleRun}>Run Task</button>
      {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
    </div>
  );
}

export default App;