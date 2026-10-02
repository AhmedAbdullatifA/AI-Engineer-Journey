# Problem 07 — Hotel Reservation System
#
# Build a small Hotel Reservation System using Object-Oriented Programming.
#
# The system should manage rooms, guests, and reservations.
# You should use multiple classes and make the objects interact with each other.
#
# You need at least four classes:
#
# 1. Room
# 2. Guest
# 3. Reservation
# 4. Hotel
#
# --
# 1. Room
# --
#
# Each Room should have:
#
# - room_number
# - room_type
# - price_per_night
# - is_available
#
# Supported room types should be:
#
# - "single"
# - "double"
# - "suite"
#
# Requirements:
#
# - room_number must be valid.
# - price_per_night must be greater than 0.
# - room_type must be one of the supported types.
# - Use @property to control access to price_per_night.
# - Changing the price should still be validated.
#
# The Room class should also have a class attribute that keeps
# track of the total number of rooms created.
#
# Example:
#
# Room.total_rooms
#
# This value should increase automatically whenever a new Room
# object is created.
#
# --
# 2. Guest
# --
#
# Each Guest should have:
#
# - name
# - email
# - phone
#
# Validate the guest information when necessary.
#
# Add a method such as:
#
# display_info()
#
# that returns the guest's information.
#
# --
# 3. Reservation
# --
#
# A Reservation represents a booking made by a Guest for a Room.
#
# Each Reservation should contain:
#
# - a Guest object
# - a Room object
# - number_of_nights
#
# The total price should be calculated based on:
#
# room.price_per_night * number_of_nights
#
# Requirements:
#
# - number_of_nights must be at least 1.
# - A reservation should only be created for an available room.
# - The room should become unavailable after a successful reservation.
#
# --
# 4. Hotel
# --
#
# The Hotel class should manage the entire reservation system.
#
# It should be able to:
#
# - Add rooms.
# - Add guests.
# - Create reservations.
# - Cancel reservations.
# - Display available rooms.
# - Display reservations for a specific guest.
#
# When a reservation is cancelled, the room should become available again.
#
# --
# Requirements
# --
#
# Your program should demonstrate:
#
# - Multiple classes
# - Object interaction
# - Composition
# - @property
# - Encapsulation
# - Class attributes
# - Validation
# - Object state management
#
# Create several objects and test the complete system at the end
# of your program.


########## Room Class

class Room :

    room_numbers = []
    total_rooms = 0
    def __init__(self, room_number, room_type, price_per_night, is_available = True ):

        # make sure the number is postive
        if room_number <= 0:
            raise ValueError("Room number must be positive")
        else:
            #make sure the number is unique
            if room_number in self.room_numbers:
                raise ValueError("Room number already exists")
            else:
                self.room_number = room_number
                Room.room_numbers.append(room_number)

        # make sure the tupe is valid
        if room_type in ["single", "double", "suite"] :
            self.room_type = room_type
        else:
            raise ValueError("The type must be \"single\", \"double\", \"suite\" ")

        # send the value to the setter function
        self.price_per_night = price_per_night
        self.is_available = is_available

        Room.total_rooms += 1

    @property
    def price_per_night(self):
        return self._price_per_night

    @price_per_night.setter
    def price_per_night(self, price_per_night):
        # make sure the price is postive
        if price_per_night <= 0:
            raise ValueError("Price per night must be positive")
        else:
            self._price_per_night = price_per_night

    



######## Guest Class 

class Guest :

    def __init__(self, name, email, phone):
        self._name = name

    # make sure its email
        if '@' in email and '.' in email.split('@')[-1] :
            self._email = email
        else : 
            raise ValueError("Invaild email")
        # maje sure its phone number
        if phone.isdigit():
            self._phone = phone
        else :
            raise ValueError("Invaild phone number")

    def display_info(self):
        return f"name : {self._name}\nphone : {self._phone}\nemail : {self._email}"

############ Reservation Class

class Reservation :

    def __init__(self, guest, room, number_of_nights):
        # make sure its object
        if isinstance(room, Room):
            self.room = room
        else:
            raise ValueError("Room must be a Room object")
            # make sure its object
        if isinstance(guest, Guest):
            self.guest = guest
        else:
            raise ValueError("Guest must be a Guest object")
        # make sure its a correct number
        if number_of_nights < 1 :
            raise ValueError("nights must be at least 1")
        else:
            self.number_of_nights = number_of_nights

        if room.is_available :
            self.total_price = room.price_per_night * number_of_nights
            room.is_available = False
        else :
            raise ValueError("The Room is already booked")


########### Hotel Class
        
class Hotel :

    def __init__(self):
        self.rooms = []
        self.guests = []
        self.reservations = []

    def add_room(self, room):
        # make sure its object
        if isinstance(room, Room):
            self.rooms.append(room)
        else:
            raise ValueError("Room must be a Room object")

    def add_guest(self, guest):
         # make sure its object
        if isinstance(guest, Guest):
            self.guests.append(guest)
        else:
            raise ValueError("Guest must be a Guest object")
        
    def create_reservation(self, guest, room, number_of_nights):
        if guest not in self.guests:
            raise ValueError("Guest not registered in this hotel")
        
        if room not in self.rooms:
            raise ValueError("Room not part of this hotel")
        
        reservation = Reservation(guest, room, number_of_nights)
        self.reservations.append(reservation)
        return reservation

    def display_available_rooms(self):
        available_room = [f"Room Number : {room.room_number} Room Type : {room.room_type} Price Per Night : {room.price_per_night}"
                          for room in self.rooms if room.is_available]
        return available_room
    
    def cancel_reservation(self, reservation):
        if reservation in self.reservations:
            self.reservations.remove(reservation)
            reservation.room.is_available = True
        else:
            raise ValueError("Reservation not found")


########## Testing

# Create a Hotel object
# Create Hotel
hotel = Hotel()

# Add Rooms
room1 = Room(101, "single", 100)
room2 = Room(102, "double", 150)
room3 = Room(103, "suite", 300)
hotel.add_room(room1)
hotel.add_room(room2)
hotel.add_room(room3)

# Add Guests 
guest1 = Guest("Ahmed", "ahmed@example.com", "0123456789")
guest2 = Guest("Sara", "sara@example.com", "9876543210")
hotel.add_guest(guest1)
hotel.add_guest(guest2)

#  Display available rooms initially 
print("Available rooms initially:")
for a in hotel.display_available_rooms():
    print(a)

#  Valid Reservation 
reservation1 = hotel.create_reservation(guest1, room1, 2)
print("\nReservation 1 created:")
print(f"Guest: {reservation1.guest.display_info()}")
print(f"Room: {reservation1.room.room_number}")
print(f"Nights: {reservation1.number_of_nights}")
print(f"Total Price: {reservation1.total_price}")

#  Try to reserve same room again (should fail) 
try:
    hotel.create_reservation(guest2, room1, 1)
except ValueError as a:
    print("\nError (double booking):", a)

#  Reserve another room 
reservation2 = hotel.create_reservation(guest2, room2, 3)
print("\nReservation 2 created:")
print(f"Guest: {reservation2.guest.display_info()}")
print(f"Room: {reservation2.room.room_number}")
print(f"Nights: {reservation2.number_of_nights}")
print(f"Total Price: {reservation2.total_price}")

#  Display available rooms after reservations 
print("\nAvailable rooms after reservations:")
for x in hotel.display_available_rooms():
    print(x)

#  Cancel Reservation 1 
hotel.cancel_reservation(reservation1)
print("\nReservation 1 cancelled.")

#  Display available rooms after cancellation 
print("\nAvailable rooms after cancellation:")
for r in hotel.display_available_rooms():
    print(r)

#  Edge Case Tests 
# Invalid guest email
try:
    bad_guest = Guest("Ali", "ali_at_example.com", "123456")
except ValueError as e:
    print("\nError (invalid email):", e)

# Invalid phone number
try:
    bad_guest2 = Guest("Omar", "omar@example.com", "phone123")
except ValueError as e:
    print("Error (invalid phone):", e)

# Invalid room type
try:
    bad_room = Room(104, "triple", 200)
except ValueError as e:
    print("Error (invalid room type):", e)

# Invalid nights
try:
    hotel.create_reservation(guest1, room3, 0)
except ValueError as e:
    print("Error (invalid nights):", e)

# Reservation with unregistered guest
try:
    outsider = Guest("John", "john@example.com", "111222333")
    hotel.create_reservation(outsider, room3, 2)
except ValueError as e:
    print("Error (guest not registered):", e)

# Reservation with room not in hotel
try:
    external_room = Room(200, "single", 120)
    hotel.create_reservation(guest1, external_room, 2)
except ValueError as e:
    print("Error (room not in hotel):", e)



# Output =>
# Available rooms initially:
# Room Number : 101 Room Type : single Price Per Night : 100
# Room Number : 102 Room Type : double Price Per Night : 150
# Room Number : 103 Room Type : suite Price Per Night : 300

# Reservation 1 created:
# Guest: name : Ahmed
# phone : 0123456789
# email : ahmed@example.com
# Room: 101
# Nights: 2
# Total Price: 200

# Error (double booking): The Room is already booked

# Reservation 2 created:
# Guest: name : Sara
# phone : 9876543210
# email : sara@example.com
# Room: 102
# Nights: 3
# Total Price: 450

# Available rooms after reservations:
# Room Number : 103 Room Type : suite Price Per Night : 300

# Reservation 1 cancelled.

# Available rooms after cancellation:
# Room Number : 101 Room Type : single Price Per Night : 100
# Room Number : 103 Room Type : suite Price Per Night : 300

# Error (invalid email): Invaild email
# Error (invalid phone): Invaild phone number
# Error (invalid room type): The type must be "single", "double", "suite" 
# Error (invalid nights): nights must be at least 1
# Error (guest not registered): Guest not registered in this hotel
# Error (room not in hotel): Room not part of this hotel