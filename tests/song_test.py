import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.songs = [
            {
                "title": "I will survive",
                "artist": "Gloria Gaynor"
            },
            {
                "title": "Come on Eileen",
                "artist": "Dexys Midnight Runners"
            }
        ]
    
    def test_songs_have_song(self):
        self.assertEqual({"title": "Come on Eileen", "artist": "Dexys Midnight Runners"}, self.songs[1])
