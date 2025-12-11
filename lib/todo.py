class Todo: 
    def __init__(self, task):
        self.task = task 
        self.completed = False #item set to false on init

    def mark_complete(self):
        self.completed = True 