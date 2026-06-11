# Build a Student class that tracks a student's name and their list of grades, and can report their average.
# Create a class called Student
# Store two attributes:
# the student's name and an empty list of grades (initialized automatically).
# Add an add_grade method
# that appends a grade (a number) to the list.
# Add a get_average method
# that prints the average of all grades — but handles the case where no grades exist yet.
# Add a get_highest method
# that prints the highest grade in the list.
# Test with two students
# who have different grades and confirm their averages are independent
class Student:

    def __init__(self,name):
        self.name = name
        self.grades = []

    def add_grade(self,grade):
        self.grades.append(grade)
        print(f"Grade of student {self.name} added")
    def get_average(self):
        if  not self.grades:
            print("First add the Grades")
            return
        else:
            total = 0
            n = len(self.grades)
            for num in self.grades:
                total += num
            average = total/n
            print(f"Required average of grades: {average}")
    def get_highest(self):
        if  not self.grades:
            print("First add the Grades")
            return
        else:
            print(f"Highest grade of {self.name}: {max(self.grades)}")
ram = Student("Ram")
shyam = Student("Shyam")
ram.add_grade(90)
ram.add_grade(40)
ram.add_grade(100)

shyam.add_grade(30)
shyam.add_grade(50)
shyam.add_grade(80)

ram.get_average()
ram.get_highest()
shyam.get_average()
shyam.get_highest()
         
        

