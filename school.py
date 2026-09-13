import json 
class Student:
    def _init_(self, name, age, course, email):
        self.name = name
        self.age = age
        self.course = course
        self.email = email
students = []
def add_student():
    name = input("Enter student name:")
    try:
        age = int(input("Enter student age:"))
    except ValueError:
        print("Invalid age!")  
        return
    if age <= 0:
        print("Age must be greater than 0.")
        return
    course = input("Enter student course:")
    Email = input("Enter student Email:")
    if "@" not in Email or "." not in Email:
        print("Invalid email")
        return
    for student in students:
        if student.name.lower() == name.lower():
            print("Student already exists.")
            return
    student = Student(name, age, course, Email)
    students.append(student)
def view_students():
    if not students:
        print("No students found")
        return
    print("\n===== Student List =====")
    for student in students:
        print("------------------------")
        print(f"Name  :{student.name}")
        print(f"Age   :{student.age}")
        print(f"Course:{student.course}")
        print(f"Email :{student.email}")
    print("------------------------")
def search_student():
      if not students:
          print("No students found.")
          return
      name = input("Enter student name to search:")
      found = False
      for student in students:
          if student.name.lower() == name.lower():
            print("------------------------")
            print(f"Name   : {student.name}")
            print(f"Age    : {student.age}")
            print(f"Course : {student.course}")
            print(f"Email  : {student.email}")
            print("------------------------")    
            found = True
            break
      if not found:
         print("Student is not found")        
def delete_student():
    if not students:
        print("No students found.")
        return
    name = input("Enter student name to delete:")
    found = False
    for student in students:
         if student.name.lower() == name.lower():
             students.remove(student)
             print("Student deleted successfully") 
             found = True
             break
    if not found:
        print("Student is not found")
def update_student():
    if not students:
        print("No students found.")
        return
    name = input("Enter student name to update:")
    found = False
    for student in students:
        if student.name.lower() == name.lower():
            found = True
            try:
                new_age = int(input("Enter new age: "))
            except ValueError:
                print("Invalid age!")
                return
            if new_age <= 0:
                print("Age must be greater than 0.")
                return
            new_course = input("Enter new course: ")
            new_email = input("Enter new email: ")
            if "@" not in new_email or "." not in new_email:
                print("Invalid email")
                return
            student.age = new_age
            student.course = new_course
            student.email = new_email
            print("Student updated successfully.")
            break
    if not found:
        print("Student is not found")    
def save_students():
    data = []
    for student in students:
        data.append({
            "name" : student.name,
            "age" : student.age,
            "course" : student.course,
            "email" : student.email
        })
    with open ("students.json" , "w") as file: 
        json.dump(data, file, indent=4 )
        print("Students saved successfully.")
def load_students():
    try:
        with open("students.json", "r") as file:
            data = json.load(file)
        for item in data:
            student = Student(
                item["name"],
                item["age"],
                item["course"],
                item["email"]
            )
            students.append(student)
    except FileNotFoundError:
        pass
load_students()       
while True:
    print("==== Student Management System ====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")
    choice = input("Enter your choice:")
    if choice == "1" :
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":    
        update_student()
    elif choice == "6":
        save_students()
        print("Program exited.")
        break
    else:
        print("Invalid choice!")