from flask import Flask, render_template, request, redirect, url_for, flash
from src.models import db
from src.task_repo import task_singleton
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
password = os.getenv('DATABASE_PASSWORD')

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{password}@localhost:5432/To_Do'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

db.init_app(app)

@app.route("/")
def index():
    allTask = task_singleton.get_all_tasks()
    
    return render_template('index.html', tasks=allTask)

@app.route('/add')
def add_todo():
    task_area = request.args.get('task_area')
    
    if not task_area:
        flash("Please enter you task", category='error')
        return redirect(url_for('index'))

    add_task = task_singleton.create_taks(task_area, False)
    
    return redirect(url_for('index'))

@app.route('/delete<int:task_id>')
def remove_task(task_id):
    get_single_task = task_singleton.get_task_by_id(task_id)
    
    db.session.delete(get_single_task)
    
    db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/finish<int:task_id>')
def finish_task(task_id):
    get_single_task = task_singleton.get_task_by_id(task_id)
    
    get_single_task.task_status = True
    
    db.session.commit()
    
    return redirect(url_for('index'))

