from flask import Flask, render_template, request, Markup
from src.models import db
from src.task_repo import task_singleton

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:{password}@localhost:5432/to_do_list'

db.init_app(app)

@app.route("/")
def index():
    return render_template('index.html')


@app.get('/')
def to_do():
    content = request.form.get('task-content')
    
    print(db.query.all())
    
    if not content:
        message = """<div class="alert alert-danger" role="alert">
  This is a danger alert—check it out!
</div>"""

    get_all_task = task_singleton.get_all_tasks()   

    return render_template('index.html', tasks=get_all_task)


# @app.get("/test")
# def test():
#     get_all_task = task_singleton.get_all_tasks()
    
#     render_template('index.html', tasks=get_all_task)