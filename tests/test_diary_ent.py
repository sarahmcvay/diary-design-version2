from lib.diary_ent import *

"""
Test that when we make a diary entry, with a date and contents it is returned
"""
def test_diary_entry_created(): 
    diary_ent = DiaryEntry("Monday", "Today I felt happy")
    assert diary_ent.date == "Monday"
    assert diary_ent.contents == "Today I felt happy"
