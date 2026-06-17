class Patient:

# Constructor takes name (required), age (required), and blood_type (optional — defaults to "Unknown").
# Validate inside __init__
    def __init__(self, name , age , blood_type = "Unknown"):
        self.__name = name
        self.__age = age
        self.__blood_type = blood_type

    def get_name(self):
        return f"Required name of patient {self.__name}"
    
    def get_age(self):
        return  {self.__age}
    
    def get_name(self):
        return f"Required name of patient {self.__blood_type}"
    
    def set_age(self,new_age):
        if new_age<= 0 or new_age > 130:
            print(f"Age should be greate than 0 and less than 130")
            return
        self.__age = new_age
        print(f"Patient age updated and become {self.__age}")
    
    def summary(self):
        print(f"Name:{self.__name}| Age:{self.__age}| Blood_Group:{self.__blood_type}")

p1 = Patient("Sara", 30, "A+")
p1.summary()

p2 = Patient("Leo", 7)
p2.summary()

p2.set_age(8)
print(f"Leo's new age: {p2.get_age()}")

    

