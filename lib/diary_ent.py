class DiaryEntry:

    def __init__(self, date, contents):
        self.date = date
        self.contents = contents
    
    def count_words(self):
        return len(self.contents.split())

    def contains_mobile(self):
        return self.contents.startswith("#MOB")



