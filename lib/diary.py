class Diary: 

    def __init__(self):
        self.entries = []
        self.mobile_list = []
    
    def all(self):
        return self.entries 
    
    def add(self, entry):
        self.entries.append(entry)
    
    def find_best_entry_for_time(self, wpm, time):
        words_user_can_read = int(wpm * time)
        can_read_now = []
        for entry in self.entries: 
            if entry.count_words() <= words_user_can_read:
                can_read_now.append(entry)
            return can_read_now[0]

    def search_mobile(self):
        for entry in self.entries: 
            if entry.contains_mobile():
                self.mobile_list.append(entry)
        return self.mobile_list

