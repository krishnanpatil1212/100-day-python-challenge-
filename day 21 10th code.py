FILE_NAME = "students.txt"

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    age = input("Enter age: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{roll},{name},{age}\n")

    print(" Student added successfully\n")


def view_students():
    try:
        with open(FILE_NAME, "r") as file:
            print("\n Student Records:")
            for line in file:
                roll, name, age = line.strip().split(",")
                print(f"Roll: {roll} | Name: {name} | Age: {age}")
    except FileNotFoundError:
        print(" No records found")
    print()


def search_student():
    search_roll = input("Enter roll number to search: ")
    found = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            roll, name, age = line.strip().split(",")
            if roll == search_roll:
                print("\n Student Found:")
                print(f"Roll: {roll}, Name: {name}, Age: {age}")
                found = True
                break

    if not found:
        print(" Student not found")
    print()

def count_students():
    count = 0
    with open(FILE_NAME, "r") as file:
        for _ in file:
            count += 1

    print(" Total Students:", count)
    print()


while True:
    print("====== STUDENT MANAGEMENT SYSTEM ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Count Students")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        count_students()
    elif choice == "5":
        print("Exiting program. Thank you!")
        break
    else:
        print("Invalid choice, try again\n")
