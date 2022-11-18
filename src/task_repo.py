from src.models import db, to_do

class tasks_to_do:
    
    def get_all_tasks(self):
        # get all tasks from the DB
        get_allMovies = to_do.query.all()
        return get_allMovies
    
    def create_taks(self, task_content):
        new_task = to_do(task_content)
        db.session.add(new_task)
        db.session.commit()
        return new_task
    
    
    
    
    
    
    

task_singleton = tasks_to_do()
    