"""
Simple To-Do List web app built with Flask.

Run locally:
    pip install -r requirements.txt
    python app.py

Then open http://127.0.0.1:5000 in your browser.
"""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage so the app runs with zero setup (no database needed).
# Each task is a dict: {"id": int, "title": str, "done": bool}
tasks = []
next_id = 1


@app.route("/")
def index():
    """Show all tasks."""
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    """Add a new task from the form."""
    global next_id
    title = request.form.get("title", "").strip()
    if title:
        tasks.append({"id": next_id, "title": title, "done": False})
        next_id += 1
    return redirect(url_for("index"))


@app.route("/toggle/<int:task_id>")
def toggle_task(task_id):
    """Mark a task as done / not done."""
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = not task["done"]
            break
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    """Remove a task."""
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
