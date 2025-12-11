from lib.diary_ent import *

"""
Test that when we make a diary entry, with a date and contents it is returned
"""
def test_diary_entry_created(): 
    diary_ent = DiaryEntry("Monday", "Today I felt happy")
    assert diary_ent.date == "Monday"
    assert diary_ent.contents == "Today I felt happy"

"""
If the diary entry contains a mobile number, with a tag '#MOB', 
it will tag the entry as True
"""
def test_if_entry_contains_mobile_mark_true():
    diary_ent = DiaryEntry("Monday", "#MOB dentist 123456789")
    result = diary_ent.contains_mobile()
    assert result == True

"""
we can use method count_words, to return number of words in contents
"""
def test_number_words_in_contents():
    diary_ent = DiaryEntry("Monday", "Today I felt happy")
    result = diary_ent.count_words()
    assert result == 4