export async function createTask(taskName) {
  const res = await fetch(`http://localhost:8000/task/${taskName}`, {
    method: "POST",
  });
  return res.json();
}