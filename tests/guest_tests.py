import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp (self):
        self.guest = Guest("Ben", 21, 42)

    def test_guest_has_name(self):
        self.assertEqual("Ben", self.guest.name )

    def test_guest_has_age(self):
        self.assertEqual(21, self.guest.age)

    def test_guest_has_wallet(self):
        self.assertEqual(42, self.guest.wallet)
