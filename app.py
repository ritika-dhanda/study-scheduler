# from flask import Flask, render_template, request, redirect
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

# app = Flask(__name__)

# # Setup database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# # Updated Task model with date field
# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(200), nullable=False)
#     date = db.Column(db.Date, nullable=False, default=datetime.utcnow)

#     def __repr__(self):
#         return f'<Task {self.id}: {self.content} - {self.date}>'

# # Home route: show tasks and add new ones
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         task_content = request.form['task']
#         task_date = request.form['date']

#         try:
#             date_obj = datetime.strptime(task_date, '%Y-%m-%d').date()
#         except ValueError:
#             date_obj = datetime.utcnow().date()

#         new_task = Task(content=task_content, date=date_obj)

#         try:
#             db.session.add(new_task)
#             db.session.commit()
#             return redirect('/')
#         except:
#             return "There was an issue adding your task."

#     else:
#         tasks = Task.query.order_by(Task.date).all()
#         return render_template('index.html', tasks=tasks)

# # Delete route
# @app.route('/delete/<int:id>')
# def delete(id):
#     task_to_delete = Task.query.get_or_404(id)

#     try:
#         db.session.delete(task_to_delete)
#         db.session.commit()
#         return redirect('/')
#     except:
#         return "There was a problem deleting that task."

# # Edit route
# @app.route('/edit/<int:id>', methods=['GET', 'POST'])
# def edit(id):
#     task = Task.query.get_or_404(id)

#     if request.method == 'POST':
#         task.content = request.form['task']
#         task_date = request.form['date']
#         try:
#             task.date = datetime.strptime(task_date, '%Y-%m-%d').date()
#         except ValueError:
#             task.date = datetime.utcnow().date()

#         try:
#             db.session.commit()
#             return redirect('/')
#         except:
#             return "There was an issue updating your task."
#     else:
#         return render_template('edit.html', task=task)

# if __name__ == "__main__":
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# Setup database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Updated Task model with date field
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<Task {self.id}: {self.content} - {self.date}>'

# Home route: show tasks and add new ones
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_content = request.form['task']
        task_date = request.form['date']

        try:
            date_obj = datetime.strptime(task_date, '%Y-%m-%d').date()
        except ValueError:
            date_obj = datetime.utcnow().date()

        new_task = Task(content=task_content, date=date_obj)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f"There was an issue adding your task: {e}"

    else:
        tasks = Task.query.order_by(Task.date).all()
        return render_template('index.html', tasks=tasks)

# Delete route
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Task.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        return f"There was a problem deleting that task: {e}"

# Edit route
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    task = Task.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['task']
        task_date = request.form['date']
        try:
            task.date = datetime.strptime(task_date, '%Y-%m-%d').date()
        except ValueError:
            task.date = datetime.utcnow().date()

        try:
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f"There was an issue updating your task: {e}"
    else:
        return render_template('edit.html', task=task)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
