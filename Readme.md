# Smart Study Scheduler

A simple Flask web application to help you manage and schedule your study tasks with due dates.  
Add, edit, delete, and mark tasks as done, all in one intuitive interface.

---

## Features

- Add tasks with a due date.
- Edit and update existing tasks.
- Delete tasks you no longer need.
- Mark tasks as completed by checking the checkbox.
- Tasks and their due dates are stored in an SQLite database.
- Responsive UI with color changes on task completion.

---

## Technologies Used

- Python 3
- Flask (Web framework)
- Flask-SQLAlchemy (Database ORM)
- SQLite (Lightweight database)
- HTML, CSS (for frontend)

---

## Project Structure
smart-study-scheduler/
│
├── app.py # Main Flask application
├── requirements.txt # Python dependencies
├── Procfile # Deployment instructions for Railway
├── templates/ # HTML templates
│ ├── index.html
│ └── edit.html
└── static/ # Static files (CSS, JS, images if any)


---

## Setup & Installation (Local)

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/smart-study-scheduler.git
   cd smart-study-scheduler
2. (Optional) Create and activate a virtual environment:

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

3. Install dependencies:
pip install -r requirements.txt

4. Run the app locally:
python app.py

5. Open your browser and go to http://127.0.0.1:5000/

## Usage
Use the input form to add a new task with a due date.

View tasks listed below with their dates.

Click Edit to update task content or date.

Click Delete to remove a task.

Check the checkbox to mark a task as done — the row color changes accordingly.