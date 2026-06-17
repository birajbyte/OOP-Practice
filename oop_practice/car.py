class Car:
    def __init__(self, brand , model ,speed = 0 , fuel = 100):
        self.brand = brand
        self.model = model
        self.__speed = speed
        self.__fuel = fuel

    def add_accelerate(self,amount):
        if self.__fuel <= 0:
            print("Out of fuel! Cannot accelerated!") 
            return
        actual = min(amount , self.__fuel)
        self.__speed += actual
        self.__fuel -= actual
        print(f"Accelerated by {actual} | Speed: {self.__speed}| Fuel:{self.__fuel}")

    def add_brake(self,amount):
        if self.__speed < amount:
            print("Speed cannot go below  Zero")
            self.__speed = 0
            return
        else:
            self.__speed -= amount
            print(f"Speed of car decrease by {amount}")
     
    def refuel(self,amount):
        self.__fuel += amount
        if self.__fuel > 100:
            print("Fuel cannot be  greater than 100")
            self.__fuel = 100
            return
        
        print(f"Fuel {amount} added successfully")

    def get_speed(self):
        return self.__speed
    
    def get_fuel(self):
        return self.__fuel
    
    def show_status(self):
        print(f"Brand:{self.brand}| Model:{self.model}| Current_speed:{self.__speed}|Fuel:{self.__fuel}")


car = Car("Toyota", "Corolla")
car.show_status()
car.add_accelerate(30)
car.add_accelerate(80)
car.add_accelerate(5)    
car.add_brake(200)       
car.refuel(999)      
car.show_status()
print(car.get_fuel())