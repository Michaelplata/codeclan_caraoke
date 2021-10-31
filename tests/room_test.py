import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Donald Duck", 30, "Duck Tale Theme Song")
        self.guest_2 = Guest("Daisy Duck", 30, "Donald's Conga")
        self.guest_3 = Guest("Daffy Duck", 20, "Giant Robot Love")
        self.guest_4 = Guest("Della Duck", 40, "Nothing can stop Della Duck")
        self.room = Room("Cartoons", 100, 3)
        self.new_song_1 = Song("I will survive")
        self.new_song_2 = Song("Do not worry, be happy")
    
    def test_room_has_theme(self):
        self.assertEqual("Cartoons", self.room.theme)
    
    def test_room_can_return_capacity(self):
        self.assertEqual(4, self.room.room_capacity)
    
    def test_can_add_songs(self):
        self.room.add_song(self.new_song_1)
        self.room.add_song(self.new_song_2)
        self.assertEqual(2, self.room.songs_count())

    def test_guest_can_check_in(self):
        self.room.check_in_guests(self.guest_1)
        self.room.check_in_guests(self.guest_2)
        self.assertEqual(2, self.room.guests_count())

    def test_guest_can_check_out(self):
        self.room.check_in_guests(self.guest_1)
        self.room.check_in_guests(self.guest_2)
        self.room.check_in_guests(self.guest_3)
        self.room.check_out_guests(self.guest_1)
        self.assertEqual(2, self.room.guests_count())

    def test_room_can_refuse_new_guest(self):
        self.room.check_in_guests(self.guest_1)
        self.room.check_in_guests(self.guest_2)
        self.room.check_in_guests(self.guest_3)
        self.room.check_in_guests(self.guest_4)
        self.room.check_in_guests(self.guest_4)
        self.assertEqual("Sorry, the room is full", self.room.refuse_new_guest())
    
    def test_room_can_take_fee(self):
        self.assertEqual(103, self.room.add_to_till())

    def test_room_can_let_room_to_guest(self):
        guest = self.guest_3
        self.room.let_room_to_guest(guest)
        self.assertEqual(1, self.room.guests_count)
        # self.assertEqual(17, self.guest_2.cash)
        self.assertEqual(103, self.room.till)






    # def test_guest_can_pay(self):
    #     self.assertEqual(17, self.reduce_cash())
    
    # def test_room_can_check_if_guest_duplicates(self):
    #     self.room.check_in_guests(self.guest_1) 
    #     self.assertEqual("You have already checked in", self.room.check_if_guest_duplicates(self.guest_1.name))
    
    


    