from lib.diary import *

"""
The diary will initially be empty 
"""
def test_the_diary_initialises():
    diary = Diary()
    assert diary.all() == []

"""
The diary will store the individual diary entries
"""
def test_the_diary_stores_entry():
    diary = Diary()
    entry_1 = "Monday", "Today I felt happy"
    diary.add(entry_1)
    assert diary.all() == [entry_1] 