import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Rock 'N' Roll")
        self.new_song_1 = Song("I will survive")
        self.new_song_2 = Song("Do not worry, be happy")
        self.new_guest_1 = Guest("Donald Duck") 
        self.new_guest_2 = Guest("Daffy Duck")
        
    def test_room_has_theme(self):
        self.assertEqual("Rock 'N' Roll", self.room.theme)
    
    def test_can_add_songs(self):
        self.room.add_song(self.new_song_1)
        self.room.add_song(self.new_song_2)
        self.assertEqual(2, self.room.songs_count())

    def test_guest_can_check_in(self):
        self.room.check_in_guests(self.new_guest_1)
        self.room.check_in_guests(self.new_guest_2)
        self.assertEqual(2, self.room.guests_count())

    def test_guest_can_check_out(self):
        self.room.check_in_guests(self.new_guest_1)
        self.room.check_in_guests(self.new_guest_2)
        self.room.check_out_guests(self.new_guest_1)
        self.assertEqual(1, self.room.guests_count())


    

    
    
    
