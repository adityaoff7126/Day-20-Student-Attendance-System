present_students = set()

def mark_attendance():
    name = input("Enter student name to mark present: ")
    
    if name in present_students:
        print("Attendance already marked.")
    else:
        present_students.add(name)
        print("Attendance marked successfully!")

def view_attendance():
    if len(present_students) == 0:
        print("No students marked present.")
    else:
        print("Students Present Today:")
        for student in present_students:
            print(student)

def check_student():
    name = input("Enter student name to check: ")
    
    if name in present_students:
        print("Student is Present.")
    else:
        print("Student is Absent.")

def remove_attendance():
    name = input("Enter student name to remove: ")
    
    if name in present_students:
        present_students.remove(name)
        print("Attendance removed.")
    else:
        print("Student not found.")

while True:
    print("\n1. Mark Attendance")
    print("2. View Attendance")
    print("3. Check Student")
    print("4. Remove Attendance")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        mark_attendance()
    elif choice == "2":
        view_attendance()
    elif choice == "3":
        check_student()
    elif choice == "4":
        remove_attendance()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice.")
