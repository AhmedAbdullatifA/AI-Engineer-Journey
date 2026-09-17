class Room:
    total_rooms = 0
    room_numbers = []
    def __init__(self, room_number, room_type, price_per_night, is_available=True):
        if isinstance(room_number,int) and room_number not in Room.room_numbers: 
            self.room_number = room_number
            Room.room_numbers.append(room_number)
        else : 
            raise ValueError("Invalid room number type , must be integer and unique")
        
        if room_type not in ["Single", "Double", "Suite"]:
            raise ValueError("Invalid room type. Must be 'Single', 'Double', or 'Suite'.")
        else :
            self.room_type = room_type

        if price_per_night <= 0:
            raise ValueError("Price per night must be greater then 0.")
        else :
            self.price_per_night = price_per_night

        self.is_available = is_available

        Room.total_rooms += 1


    @property
    def price_per_night(self):
        return self._price_per_night

    @price_per_night.setter
    def price_per_night(self, price_per_night):
        if price_per_night <= 0:
            raise ValueError("Price per night must be greater then 0.")
        else:
            self._price_per_night = price_per_night            


r1 = Room(101, "Single", 100)
r2 = Room(171, "Single", 102)
r3 = Room(181, "Single", 103)

print(r3)
print(r3.total_rooms)
