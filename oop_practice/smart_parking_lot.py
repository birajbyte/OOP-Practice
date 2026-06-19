class Vehicle:
    
    def __init__(self, license_plate , vehicle_type):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

class Car(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate , "Car")
class Motorcycle(Vehicle):
       def __init__(self, license_plate):
        super().__init__(license_plate , "Bike")

class ParkingSpot:

    def __init__(self, spot_number , spot_type , is_occupied = False , current_vehicle = None):
        self.spot_number = spot_number
        self.spot_type = spot_type
        self.is_occupied = is_occupied
        self.current_vehicle = current_vehicle

class ParkingLot:

    def __init__(self, name):
        self.name = name
        self.slots = []

    def add_slot(self , spot):
        self.slots.append(spot)
        
    def park_vehicle(self , vehicle):
        if not self.slots:
            print("Parking slots are not added yet")
            return
        for spot in self.slots:
            if not  spot.is_occupied:
                if vehicle.vehicle_type.lower() == "car" and spot.spot_type.lower() == "compact":
                    spot.is_occupied = True
                    spot.current_vehicle = vehicle
                    print(f"Car parked successfully on the spot_number :{spot.spot_number}")
                    return

                elif vehicle.vehicle_type.lower() == "bike":
                    spot.is_occupied = True
                    spot.current_vehicle = vehicle
                    print(f"Bike parked successfully on the spot_number :{spot.spot_number}")
                    return
                
            
        print("Sorry, no available spots matching your vehicle type!")

    def leave_parking_spot(self, license_plate, hours_parked):
        if not self.slots:
            print("Parking spots arenot added yet!")
            return
        for spot in self.slots:
            if spot.is_occupied:
                if spot.current_vehicle.license_plate == license_plate:

                    if spot.spot_type.lower() == "compact" and spot.current_vehicle.vehicle_type.lower() == "car":
                        rate = 5
                        bill = hours_parked * rate
                        v_type = "car"
                    else:
                        rate = 2
                        bill = hours_parked * rate
                        v_type = "bike"
                    
                    print("=" * 10)
                    print(" Total Bill")
                    print("=" * 10)
                    print(f"Total Bill ${bill} at rate ${rate} for {v_type} and spot {spot.spot_number}")

                    spot.is_occupied = False
                    spot.current_vehicle = None
                    return
        print("Invalid Liscense_plate")

garage = ParkingLot("Central Parking Birtamode")
# 2. Automatically generate 5 Bike spots (Spots 101 to 105)
for i in range(1,3):#when slot not avaiable bike take slot of car 201 if 
    spot = ParkingSpot(spot_number = 100+i , spot_type = "Bike")
    garage.add_slot(spot)
# 2. Automatically generate 5 Car spots (Spots 101 to 105)           
for i in range(1,6):
    spot = ParkingSpot(spot_number = 200+i , spot_type = "Compact")
    garage.add_slot(spot)

# print("\n--- STARTING TEST CASES ---")

# # --- CASE 1: Standard Car Parking & Leaving ---
# print("\n[Test 1] Parking a regular Car...")
# car1 = Car("BA-1-PA-2026")
# garage.park_vehicle(car1)  # Should look for and find Compact spot 201

# print("\n[Test 2] Car leaving after 4 hours...")
# garage.leave_parking_spot("BA-1-PA-2026", hours_parked=4)

print("\n[Test 3] Filling up Bike spots to test flexibility...")
bike1 = Motorcycle("ME-2-RA-9999")
bike2 = Motorcycle("BA-5-PA-1111")
bike3 = Motorcycle("ORANGE-NS200") # A third bike arrives!

garage.park_vehicle(bike1)  # Takes Bike spot 101
garage.park_vehicle(bike2)  # Takes Bike spot 102
garage.park_vehicle(bike3)

# --- CASE 3: Leaving from an adapted spot ---
print("\n[Test 4] Third bike leaves after 5 hours...")
# This bike is in a Compact spot, but your code dynamically checks the spot type 
# to charge it. Let's see if it bills $25 (Compact rate) or handles it!
garage.leave_parking_spot("ORANGE-NS200", hours_parked=5)

print("\n[Test 5] Trying to remove a vehicle that doesn't exist...")
garage.leave_parking_spot("FAKE-PLATE-123", hours_parked=2)






                    

        
    
