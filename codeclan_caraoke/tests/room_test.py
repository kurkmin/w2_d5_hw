import unittest
from classes.room import Room 
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(1, 4)
    
    def test_has_room_number(self):
        self.assertEqual(1, self.room.number)

    def test_has_guests_in_room(self):
        self.assertEqual([], self.room.guests)

    def test_check_in(self):
        guest1 = Guest("Sumin", 20)
        guest2 = Guest("John", 10)
        self.room.check_in(guest1)
        self.room.check_in(guest2)
        self.assertEqual(True, self.room.can_check_in()) 
        self.assertEqual(True, self.room.can_guest_pay(guest1))
        self.assertEqual(["Sumin", "John"], self.room.guests)

    def test_check_out(self):
        guest1 = Guest("Sumin", 20)
        guest2 = Guest("John", 10)
        self.room.check_in(guest1)
        self.room.check_in(guest2)
        self.room.check_out(guest1)
        self.room.check_out(guest2)
        self.assertEqual([], self.room.guests)

    def test_add_song(self):
        song1 = "Hello"
        song2 = "Often"
        self.room.add_song(song1)
        self.room.add_song(song2)
        self.assertEqual(["Hello", "Often"], self.room.songs)

    def test_can_check_in_(self):
        guest1 = Guest("Sumin", 20)
        guest2 = Guest("John", 10)
        guest3 = Guest("James", 5)
        guest4 = Guest("Tiwa", 0) 
        self.room.check_in(guest1)
        self.room.check_in(guest2)
        self.room.check_in(guest3)
        self.room.check_in(guest4)
        self.assertEqual(True, self.room.can_check_in())

    def test_can_not_check_in(self):
        guest1 = Guest("Sumin", 20)
        guest2 = Guest("John", 10)
        guest3 = Guest("James", 5)
        guest4 = Guest("Tiwa", 0) 
        guest5 = Guest("Alexandra", 20)
        self.room.check_in(guest1)
        self.room.check_in(guest2)
        self.room.check_in(guest3)
        self.room.check_in(guest4)
        self.room.check_in(guest5)
        self.assertEqual(False, self.room.can_check_in())

    def test_can_guest_pay(self):
        guest1 = Guest("Sumin", 20)
        self.assertEqual(True, self.room.can_guest_pay(guest1))

    def test_can_guest_pay(self):
        guest3 = Guest("James", 5)
        self.assertEqual(False, self.room.can_guest_pay(guest3))


        
    
