from lib.diary import *
from lib.todo_list import *
from lib.diary_ent import *


"""
when two diary entries are entered, the diary will return both
"""
def test_diary_holds_all_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Monday", "Today I felt happy")
    entry_2 = DiaryEntry("Tuesday", "Today I felt truely amazing, best day ever")
    diary.add(entry_1)
    diary.add(entry_2)
    result = diary.all()
    assert result == [entry_1, entry_2]

"""
The diary can pull up a list of mobile numbers across all diary entries
"""
def test_mobile_list_is_returned():
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
"""
def test_entry_that_can_be_read_in_time_given_returned_for_reflection():
    diary = Diary()
    entry_1 = DiaryEntry("Monday", "Today I felt happy")
    entry_2 = DiaryEntry("Tuesday", "Today I felt truely amazing, best day ever")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_time(2, 2) == entry_1
#   (2, wpm ; 2, minutes to read) 
