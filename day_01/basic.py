class Student:
    # The setup instructions
    def __init__(self,name,roll):
        self.name = name  # Saves the name inside the specific object
        self.roll = roll
    def say_hello(self):
        return f"Hello, my name is {self.name}"
# Creating objects with unique names
user_input1 = input("Enter the name of Student ")
student1 = Student(user_input1,3)
user_input2 = input("Enter the name of student ")
student2 = Student(user_input2,4)

# Viewing the output
print(student1.say_hello())  # Output: Alice
print(student2.say_hello()) 
print(student1.roll)