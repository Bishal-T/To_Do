from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class to_do(db.Model):
    task_id = db.Column('task_id',db.Integer, primary_key=True)
    task_content = db.Column(db.String, nullable=False)
    
    
    def __init__(self, task_content):
        self.task_content = task_content
        
        
        
  