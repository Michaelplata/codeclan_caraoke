from classes.guest import Guest
from classes.song import Song


class Room:
    
    def __init__(self, theme, till, fee):
        self.theme = theme
        self.till = till
        self.songs = []
        self.guests = []
        self.room_capacity = 4
        self.fee = fee
    
    def get_room_theme(self):
        return self.theme

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
   
    def refuse_new_guest(self):
        while self.room_capacity >= len(self.guests):
            self.check_in_guests()
        else: 
            return "Sorry, the room is full"
   
    def add_to_till(self):
        self.till += self.fee
        return self.till
   
    def let_room_to_guest(self, guest):
        
        self.check_in_guests(guest)
        # Guest.reduce_cash(self.fee)
        self.add_to_till(self.fee)
        
   
   
   
   
   
    # def check_if_guest_duplicates(self, guest):
    #     for guest in self.guests:
    #         if self.guests[guest] == guest:
    #             return "You have already checked in"
    



