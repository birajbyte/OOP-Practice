class Animal:
    def __init__(self, name , sound):
        self.name = name 
        self.sound = sound

    def speak(self):
        print(f"{self.name} says {self.sound}")
    
    def describe(self):
        print(f"I am {self.name}")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "woof")

    def fetch(self,item):
        print(f"{self.name} fetches {item}!")

class Cat(Animal):
    def __init__(self,name , is_indoor = True):
        super().__init__(name, "Meow")
        self.indoor = is_indoor
    
    def speak(self):
        super().speak()
        print("and looks impressed")

dog = Dog("Rex")
cat = Cat("Luna",True )

dog.speak()            # inherited from Animal
dog.fetch("ball")       # Dog-specific
dog.describe()         # inherited from Animal

cat.speak()           # Cat's overridden version
cat.describe()         # inherited from Animal
print(f"Luna is indoor: {cat.indoor}")

class Bird(Animal):
    def __init__(self, name, can_fly = True):
        super().__init__(name, "any")
        self.fly = can_fly

    def can_fly(self):
        if  not self.fly:
            print(f"Bird {self.name} can't fly")
            return
        else:
            print(f"Bird {self.name} can fly")

bird = Bird("Penguine", False)

bird.can_fly()



