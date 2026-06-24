#we will try multi inheritance here
class Parent1:
    def __init__(self):
        print("Access given to Parent1 constructor")
    def describe(self):
        print("Access to parent1 method")

class Parent2:
    def __init__(self):
        print("Access given to Parent2 constructor")
    def describe(self):
        print("Access to parent2 method")
    
class Child(Parent1,Parent2):#we have learned python read parent from left to right 
    def __init__(self):
        super().__init__()
        print("Done")
obj = Child()
obj.describe()

