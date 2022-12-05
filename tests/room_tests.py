import unittest
from classes.song import Song
from classes.room import Room
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp (self):
       
        self.song1 = Song("Salute","Joy")
        self.song2 = Song("Mall Grab","love Reigns")
        self.song3 = Song("Taylor Swift", "22")
        self.song4 = Song("Ed Sheeran", "18") 
        self.song5 = Song("skin on skin", "Burn dem bridges") 
        collection_of_songs = [self.song1, self.song2, self.song3, self.song4]
        self.guest1 = Guest("Ben", 21, 42)
        self.guest2 = Guest("Mina", 22, 65)
        self.guest3 = Guest("Rosie", 15, 34)
        self.guest4 = Guest("Lorna", 25, 120)
        self.guest5 = Guest("Max", 24, 250)
        guest_list = [self.guest1, self.guest2, self.guest3, self.guest4]
        self.room = Room(guest_list, collection_of_songs, 25, 200, 6)
    
    def test_room_has_a_cost(self):
        self.assertEqual(25, self.room.cost_of_room)

    def test_check_in_guest(self):
        self.room.check_in_guest(self.guest5)
        self.assertEqual(5, len(self.room.guest_list))

    def test_check_out_guest(self):
        self.room.check_out_guest(self.guest4)
        self.assertEqual(3, len(self.room.guest_list))

    def test_add_song_to_collection_of_songs(self):
        self.room.add_song(self.song5)
        self.assertEqual(5, len(self.room.collection_of_songs))

    def test_remove_song_from_collection_of_songs(self):
        self.room.remove_song(self.song2)
        self.assertEqual(3, len(self.room.collection_of_songs))

    def test_increase_till(self):
        self.room.increase_till(50)
        self.assertEqual(250, self.room.till)

    def test_decrease_till(self):
        self.room.decrease_till(50)
        self.assertEqual(150, self.room.till)

    def test_check_number_of_guests(self):
        self.assertEqual(4, len(self.room.guest_list))

    def test_guest_pays_for_entry(self):
        self.room.pay_entry(self.room.cost_of_room)
        self.assertEqual(225, self.room.till)
        self.assertEqual(40, self.guest2.wallet)
    
    # def test_check_number_of_guest_is_below_capacity(self):
    #     num_of_guests = self.test_check_number_of_guests()
    #     self.room.check_number_of_guests_is_below_capcity(num_of_guests)
    #     self.assertEqual(4, len(self.room.guest_list))
    #     self.assertEqual("Your booking is confirmed", self.room.check_number_of_guests_is_below_capcity())






    
