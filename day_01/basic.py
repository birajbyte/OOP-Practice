class Student:
    def __init__(self,name,faculty):
        self.name = name
        self.faculty = faculty
    
    def view(self):
        return f"Student name {self.name} | Faculty {self.faculty}"
    def __repr__(self):
        return f"Student('{self.name}','{self.faculty}')"
  #Store the data  
classroom = []
for i in range(3):
    print(f"The details of student {i+1}")
    user_input1 = input("Enter the name ")
    user_input2 = input("Enter the Faculty ")
    new_student = Student(user_input1,user_input2)
    classroom.append(new_student)
#now process to see the data

print(f"\n{"="*100}")
print("                 CLASSROOM B-TECH                             ")
print(f"\n{"="*100}")
for student in classroom:
    print(student.view())

print(f"/n{"="*100}")
print("                 SEARCH SYSTEM                                            ")
print(f"/n{"="*100}")
query = input("Enter the name of to  search in classroom  ")
for student in classroom:
    if student.name.lower() == query.lower():
        print("\n Match found")
        print(student.view())
        break
else:
    print("Error not found enter correct name")
print(f"/n{"="*100}")
print("        Delete System                        ")
query_delete = input("Enter the name to remove ")
for student in classroom:
    if student.name.lower() == query_delete.lower():
        classroom.remove(student)
        print(f"Student record {student.name} deleted")
        break
else:
    print("Enter the valid name ")

print(classroom)