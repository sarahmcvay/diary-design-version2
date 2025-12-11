class TodoList: 
    def __init__(self):
        self.list_todo = []

    def add(self, entry):
        self.list_todo.append(entry)

    def incomplete(self):
        self.incomplete_list = []
        for entry in self.list_todo:
            if entry.completed == False:
                self.incomplete_list.append(entry) 
        return self.incomplete_list

    def complete(self):
        self.completed_list = []
        for entry in self.list_todo:
            if entry.completed == True:
                self.completed_list.append(entry) 
        return self.completed_list

    def give_up(self):
        for entry in self.list_todo:
            entry.mark_complete()