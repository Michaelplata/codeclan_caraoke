class Room:
    
    def __init__(self, theme):
        self.theme = theme
        self.songs = []
        self.guests = []
    
    def songs_count(self):
        return len(self.songs)
    
    def add_song(self, new_song):
        self.songs.append(new_song)
    
    def guests_count(self):
        return len(self.guests)
    
    def check_in_guests(self, guest):
        self.guests.append(guest)
    
    def check_out_guests(self, guest):
        self.guests.remove(guest)



