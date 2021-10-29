import unittest
from classes.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.theme_1 = Room("Popstars")
        self.theme_2 = Room("80's Night")
        self.theme_3 = Room("Rock 'N' Roll")
    
    def test_room_has_theme(self):
        self.assertEqual("Rock 'N' Roll", self.theme_3.theme)
        
    

    
    
    
