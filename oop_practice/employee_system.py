# Create Employee base class with:
# →  name, salary attributes
# →  work() method
# →  get_details() method
class Employee:

    def __init__(self, name , salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} is working")

    def get_details(self):
        print(f"Name:{self.name}|Salary:{self.salary}")

    def calculate_salary(self):
        print(f"Salary of {self.salary}")

class FullTime(Employee):

    def __init__(self, name , salary, bonus):
         super().__init__(name, salary)
         self.bonus = bonus
    
    def work(self):
        print(f"{self.name} is working 9am to 5 pm")

    def get_details(self):
        print(f"Name:{self.name}|Salary:{self.salary}")
    def calculate_salary(self):
        print(f"Salary of {self.name}:{self.salary+self.bonus}")
    
       
    

class PartTime(Employee):
    def __init__(self, name , salary ,hours_worked):
        super().__init__(name , salary)
        self.hours_worked = hours_worked
    
       
    def work(self):
        print(f"{self.name} is working partime for {self.hours_worked} per hrs")

    def get_details(self):
        print(f"Name:{self.name}|Salary:{self.salary} per hour")
    def calculate_salary(self):
        print(f"Salary of {self.name}:{self.salary * self.hours_worked} works partime")

emp1 = FullTime("Biraj", 50000, 5000)
emp2 = PartTime("Ram", 500, 40)
emp3 = FullTime("Sita", 45000, 3000)

emp1.calculate_salary()
emp2.calculate_salary()

employees = [emp1, emp2, emp3]
for emp in employees:
    emp.work()  

print(emp1.name)
print(emp2.hours_worked)    

emp4 = Employee("John", 30000)  
emp4.get_details()
        

        
# Create FullTime, PartTime children:
# →  FullTime has bonus attribute
# →  PartTime has hours_worked
# →  each calculates salary differently

# Test with multiple objects! 

