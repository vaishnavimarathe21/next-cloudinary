students = {}
def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    grade = input("Enter grade: ")
    students[name] = {"age": age, "grade": grade}
def update_student():
    name = input("Enter name: ")
    if name in students:
        age = int(input("New age: "))
        grade = input("New grade: ")
        students[name] = {"age": age, "grade": grade}
def delete_student():
    name = input("Enter name: ")
    if name in students:
        del students[name]
def display_students():
    for name, info in students.items():
        print(f"{name}: {info}")
while True:
    print("1.Add 2.Update 3.Delete 4.Display 5.Exit")
    choice = input("Choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        update_student()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        display_students()
    elif choice == "5":
        break
