from classes.guest import Guest
class Room:

    def __init__(self, guest_list, collection_of_songs, cost_of_room, till, capacity):
        self.guest_list = guest_list
        self.collection_of_songs = collection_of_songs
        self.cost_of_room = cost_of_room
        self.till = till
        self.capacity = capacity

    def check_in_guest(self, guest):
        self.guest_list.append(guest)
    
    def check_out_guest(self, guest):
        self.guest_list.remove(guest)
    
    def add_song(self, song):
        self.collection_of_songs.append(song)

    def remove_song(self,song):
        self.collection_of_songs.remove(song)

    def increase_till(self, amount):
        self.till += amount

    def decrease_till(self, amount):
        self.till -= amount
    
    def check_number_of_guests(self):
        return len(self.guest_list) 

    def pay_entry(self):
        self.increase_till(self, self.cost_of_room)   
        
        
       
    # def check_number_of_guests_is_below_capcity(self):
    #     number_of_guests = self.check_number_of_guests(self)
    #     if number_of_guests > 6:
    #         return "This room is maximum capacity"
    #     else:
    #         return "Your booking is confirmed"

        



        
        