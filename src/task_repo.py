from src.models import db, to_do

class tasks_to_do:
    
    def get_all_tasks(self):
        get_allTask = to_do.query.all()
        return get_allTask
    
    def create_taks(self,task_content, task_status):
        new_task = to_do(task_content, task_status)
        db.session.add(new_task)
        db.session.commit()
        return new_task
    
    def get_task_by_id(self, task_id):
        return to_do.query.get(task_id)


task_singleton = tasks_to_do()
    