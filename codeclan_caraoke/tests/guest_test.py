import unittest
from classes.guest import Guest 

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Sumin", 20)
    
    def test_has_guest_name(self):
        self.assertEqual("Sumin", self.guest.name)
