import unittest
from classes.guest import Guest
from classes.room import Room

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Donald Duck", 30, "Duck Tale Theme Song")
        
    def test_guest_has_name(self):
        self.assertEqual("Donald Duck", self.guest.name)

    def test_guest_has_cash(self):
        self.assertEqual(30, self.guest.cash)
    
    def test_guest_has_favourite_song(self):
        self.assertEqual("Duck Tale Theme Song", self.guest.favourite_song)
    
    def test_can_reduce_cash(self):
        self.guest.reduce_cash(3)
        self.assertEqual(27, self.guest.cash)