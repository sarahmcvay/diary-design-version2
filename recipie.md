DESCRIPTION OF THE CHALLENGE
As a user:
    - So I can record my experiences, I want to keep a regular diary
    - So I can reflect on experiences, I want to read past entries
    - So I can reflect even on a busy day, 
        I want to select diary entries based on how much time I have and reading speed
    - So I can keep track of my tasks, I want a todo list along with my diary
    - So I can keep a track of my contacts, I want to see a list of mobile numbers in my diary entries

CLASS INTERFACE
```python
class Calendar:
# class knows about both the diary and the todo list
# allows for easy calling of objects from either diary or todo. 

class Diary: 
# store all the diary entries
def __init__(self, entry):
    pass

# will need to add the diary entries 
def add():
    pass

# will need to list, recall the entries
def format():
    pass

# will need to select a diary entry based on time we have to read
def best_read():
    pass

# will be able to create a list of entries with mobile numbers 
def search_mobile():
    pass 

# maybe: call the items on the todo list from the diary function? 
# maybe: mentions wanting to keep a regular diary, can we datestamp, or say how many times an entry was made this week/month? 

class DiaryEntry:
# will create an inidividual diary entry
def __init__(self):
    pass 

# will mark as true if it contains a mobile number
def contains_mobile():
    pass 

# maybe will mark as true if it contains a todo item  def contains_todo(): pass 

class TodoList:
# will store todo items
def __init__():
    pass

# will add todos that are not complete
def add():
    pass 

# will list only items that we still need to do

class Todo:
# will create an individual todo task and mark as incomplete (False) on initialization
def __init__():
    pass
# will mark as true when the todo is done 
def completed():
    pass 

```