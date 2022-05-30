import unittest 
from classes.song import Song 

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Hello")
    
    def test_has_song_name(self):
        self.assertEqual("Hello", self.song.name)