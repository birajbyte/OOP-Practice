#vehile management system
class Vehicle:#keep variable and parameter name same like self.is_avaiable = is_avaiable

    def __init__(self,brand,model,rate,is_avaiable = True):
        self.brand = brand
        self.model = model
        self.__rental_rate = rate
        self.avaiable = is_avaiable
    
    def get_rental_rate(self):
        return self.__rental_rate
    def set_rental_rate(self,new_rate):
        if new_rate <= 0:
            print("Rate musht be greate than zero")
            return
        else:
            self.__rental_rate = new_rate
            print(f"Rental rate for model {self.model} implemented: {new_rate}")
    def display_features(self):
        print(f"Brand:{self.brand}|Model:{self.model}|Rate:{self.get_rental_rate()} per hour")

class Car(Vehicle):
    def __init__(self, brand, model, rate, is_avaiable=True, doors = 4):
        super().__init__(brand, model, rate, is_avaiable)
        self.doors = doors
    
    def display_features(self):
        super().display_features()
        print(f"Doors:{self.doors}")

class Motorcycle(Vehicle):
    def __init__(self, brand , model , rate , is_avaiable = True , engine_cc = 125):
        super().__init__(brand , model , rate , is_avaiable)
        self.engine = engine_cc

    def display_features(self):
        super().display_features()
        print(f"Engine_cc:{self.engine}")
class RentalStore:

    def __init__(self,name):
        self.name = name
        self.fleet = []

    def add_vehicle(self,vehicle):
        self.fleet.append(vehicle)
        print(f"Vehicle added to  Store:{self.name} Successfully")
    
    def show_fleet(self):
        if not self.fleet:
            print("First add vehicle")
            return
        else:
            for v in self.fleet:
                v.display_features()
    
    def rent_vehicle(self , model , days):
        if not self.fleet:
            print("First add vehicle to store!!")
            return
        for vehicle in self.fleet:
            if vehicle.model.lower()== model.lower():
                if vehicle.avaiable:
                    vehicle.avaiable = False
                    total_cost = vehicle.get_rental_rate() * days * 24
                    print(f"Total rent_cons {total_cost}  for {days} days ")
                    return
                else:
                    print(f"The required vehicle with model:{vehicle.model} is already rented out ")
                    return
        print(f"Required vehicle model not found in {self.name}")
                
    def return_vehicle(self, model):
        for vehicle in self.fleet:
            if vehicle.model == model:
                vehicle.avaiable = True
                print("Vehicle  Returned successfully")
                return
        else:
            print(f"Invalid model name {model}")
             
# Create specific vehicle objects
car1 = Car("Hyundai", "i20", 40, doors=4)
bike1 = Motorcycle("Bajaj", "Pulsar NS200", 25, engine_cc=200)
bike2 = Motorcycle("Yamaha", "FZ-S", 22, engine_cc=149)
my_store = RentalStore("Biraj_Rental")
#     # Add vehicles to the store list
# print("--- Registering Vehicles ---")
my_store.add_vehicle(car1)
my_store.add_vehicle(bike1)
my_store.add_vehicle(bike2)
    # Show the entire fleet using our custom loop
my_store.show_fleet() 
my_store.rent_vehicle("Pulsar NS200",3)
my_store.return_vehicle("Pulsar NS200")
     

