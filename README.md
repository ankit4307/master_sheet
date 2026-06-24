# 📝 Flask To-Do App

A simple to-do list web application built with Python and Flask. Add tasks, mark them as done, and delete them — all from a clean web interface.

## Features

- Add new tasks
- Mark tasks as done / not done (click the task title)
- Delete tasks
- Clean, responsive design

> Note: Tasks are stored **in memory**, so they reset every time you restart the app. This keeps setup simple (no database needed). See "Next Steps" below to make data persistent.

## Project Structure

```
flask-todo-app/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── README.md
├── .gitignore
├── templates/
│   ├── base.html       # Shared layout
│   └── index.html      # Task list page
└── static/
    └── style.css       # Styles
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/flask-todo-app.git
cd flask-todo-app
```

### 2. (Recommended) Create a virtual environment

```bash
python -m venv venv
# On macOS / Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```

Open your browser and go to: **http://127.0.0.1:5000**

## Next Steps (Optional Ideas)

- Add a database (SQLite + Flask-SQLAlchemy) so tasks persist
- Add edit functionality for existing tasks
- Add due dates or priorities
- Deploy to a platform like Render, Railway, or PythonAnywhere

## License

Free to use and modify.
