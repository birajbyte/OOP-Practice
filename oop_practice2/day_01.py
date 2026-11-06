'''1)Build a Student class with name and marks.
 Add a method has_passed() that returns True if marks ≥ 40.'''
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def has_passed(self):
        return self.marks >= 40

prabesh = Student('Prabesh',40)
print(f"Has passed: {prabesh.has_passed()}")

#Create a Rectangle class with width and height. Add methods area() and perimeter().
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height         
    def perimeter(self):
        return 2*(self.width + self.height)
a = Rectangle(10,20)
print(f"Area of rectangle:{a.area()}")
print(f"Perimeter of rectangle:{a.perimeter()}")

'''Make a Car class with attributes brand and speed.
 Add a method show() that prints them nicely'''
print()
class Car:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed
    def show(self):
        print(f"Brand {self.brand} has speed {self.speed}")
car = Car("BMW",300)
car.show()
'''Create a Book class with title and author.
 Instantiate 3 books and print all their titles using a loop.'''
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    
book1 = Book('a','b')
book2 = Book('c','d')
book3 = Book('d','e')

books = [book1,book2,book3]
for book in books:
    print(f"Book_Title:{book.title}||Author:{book.author}")
