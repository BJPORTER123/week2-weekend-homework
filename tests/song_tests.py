import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp (self):
        self.song= Song("Joy", "Salute")
    
    def test_song_has_artist(self):
        self.assertEqual("Salute", self.song.song_name)
    
    def test_song_has_name(self):
        self.assertEqual("Joy", self.song.artist_name)

  