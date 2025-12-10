from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    due_date = db.Column(db.String(20))
    priority = db.Column(db.Integer, default=1)
    estimated_time = db.Column(db.Float, default=0)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Task {self.description}>"
