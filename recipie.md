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
def __init__(self):
    pass

# will need to add the diary entries, str 
def add(self, entry):
    pass

# will need to list all entries, recall the entries
def all(self):
    pass

# will need to select a diary entry based on time we have to read
def best_read(self, wpm, time):
    pass

# will be able to create a list of entries with mobile numbers 
def search_mobile(self):
    pass 

# maybe: call the items on the todo list from the diary function? 
# maybe: mentions wanting to keep a regular diary, can we datestamp, or say how many times an entry was made this week/month? 

class DiaryEntry:
# will create an inidividual diary entry
def __init__(self, date, contents):
    pass 

# we can count words in diary contents
def count_words(self)

# will mark as true if it contains a mobile number
def contains_mobile(self):
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

EXAMPLE TESTS 
"""
The diary will initially be empty 
(diary)"""
test_the_diary_initialises():
    diary = Diary()
    assert diary.all() == []

"""
The diary will store the individual diary entries
(diary)"""
test_the_diary_stores_entry():
    diary = Diary()
    entry_1 = "Monday", "Today I felt happy"
    diary.add(entry_1)
    assert diary.all() == [entry_1] 

"""
Test that when we make a diary entry, with a date and contents it is returned
(diary entry)"""
test_diary_entry_created(): 
    diary_ent = DiaryEntry("Monday", "Today I felt happy")
    assert diary_ent.date == "Monday"
    assert diary_ent.contents == "Today I felt happy"

"""
If the diary entry contains a mobile number, with a tag '#MOB', 
it will tag the entry as True
(diary entry)"""
test_if_entry_contains_mobile_mark_true():
    diary_ent = DiaryEntry("Monday", "#MOB dentist 123456789")
    result = diary_ent.contains_mobile()
    assert result == True

"""
we can use method count_words, to return number of words in contents
(diary entry)"""
test_number_words_in_contents():
    diary_ent = DiaryEntry("Monday", "Today I felt happy")
    result = diary_ent.count_words()
    assert result == 4

"""
when two diary entries are entered, the diary will return both
(integration)"""
test_diary_holds_all_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Monday", "Today I felt happy")
    entry_2 = DiaryEntry("Tuesday", "Today I felt truely amazing, best day ever")
    diary.add(entry_1)
    diary.add(entry_2)
    result = diary.all()
    assert result == [entry_1, entry_2]

"""
The diary can pull up a list of mobile numbers across all diary entries
(integration)"""
test_mobile_list_is_returned():
    diary = Diary()
    entry_1 = DiaryEntry("Monday", "Today I felt happy")
    entry_2 = DiaryEntry("Tuesday", "#MOB Dentist 123456789")
    entry_3 = DiaryEntry("Tuesday", "#MOB Vet 987654321")
    entry_4 = DiaryEntry("Tuesday", "Today I felt truely amazing, best day ever")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    diary.add(entry_4)
    result = diary.search_mobile()
    assert result == [entry_2, entry_3]

"""
when given spare minutes and reading speed wpm, 
the diary will return the best diary entry to reflect on at the moment, 
i.e. as long as possible but not too long for the time given
(integration)"""
test_entry_that_can_be_read_in_time_given_returned_for_reflection():
    diary = Diary()
    entry_1 = DiaryEntry("Monday", "Today I felt happy")
    entry_2 = DiaryEntry("Tuesday", "Today I felt truely amazing, best day ever")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_time(2, 2) == entry_1
#   (2, wpm ; 2, minutes to read) 

```