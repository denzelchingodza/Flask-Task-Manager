from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Task
import webbrowser

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # needed for flash messages
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Handle Add Task form submission
        description = request.form['description']
        due_date = request.form['due_date']
        priority = int(request.form['priority'])
        estimated_time = float(request.form['estimated_time'])
        task = Task(description=description, due_date=due_date,
                    priority=priority, estimated_time=estimated_time)
        db.session.add(task)
        db.session.commit()
        flash("Task added successfully!", "success")
        return redirect(url_for('index'))

    # GET request: show tasks
    filter_status = request.args.get('filter', 'all')
    if filter_status == 'completed':
        tasks = Task.query.filter_by(completed=True).order_by(Task.priority.desc()).all()
    elif filter_status == 'pending':
        tasks = Task.query.filter_by(completed=False).order_by(Task.priority.desc()).all()
    else:
        tasks = Task.query.order_by(Task.priority.desc()).all()

    # Return template for GET requests
    return render_template("index.html", tasks=tasks, filter_status=filter_status)

@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if request.method == "POST":
        task.description = request.form['description']
        task.due_date = request.form['due_date']
        task.priority = int(request.form['priority'])
        task.estimated_time = float(request.form['estimated_time'])
        db.session.commit()
        flash("Task updated successfully!", "success")
        return redirect(url_for('index'))
    return render_template("edit_task.html", task=task)

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash("Task deleted successfully!", "danger")
    return redirect(url_for('index'))

@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = True
    db.session.commit()
    flash("Task marked as completed!", "success")
    return redirect(url_for('index'))

if __name__ == "__main__":
    print("Starting Flask app...")
    # Open browser automatically
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True)




