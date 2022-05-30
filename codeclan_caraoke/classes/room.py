class Room:
    def __init__(self, number, max_entry):
        self.number = number 
        self.max_entry = max_entry
        self.guests = []
        self.songs = []
        self.entry_fee = 10
    def check_in(self, guest):
        self.guests.append(guest.name)
    
    def check_out(self, guest):
        self.guests.remove(guest.name)

    def add_song(self, song):
        self.songs.append(song)

    def can_check_in(self):
        if self.max_entry < len(self.guests):
            return False
        return True 
    
    def can_guest_pay(self, guest):
        if self.entry_fee > guest.cash:
            return False
        return True 