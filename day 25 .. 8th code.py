import json
import os
import hashlib
import datetime
import statistics
import logging
import random


DATA_FILE = "advanced_database.json"
LOG_FILE = "system.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)



def generate_id(prefix):
    return f"{prefix}{random.randint(10000,99999)}"


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class Database:
    def __init__(self):
        if not os.path.exists(DATA_FILE):
            self.data = {
                "users": [],
                "students": [],
                "attendance": [],
                "marks": []
            }
            self.save()
        else:
            self.load()

    def load(self):
        with open(DATA_FILE, "r") as f:
            self.data = json.load(f)

    def save(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.data, f, indent=4)

    def add(self, table, record):
        self.data[table].append(record)
        self.save()

    def get(self, table):
        return self.data[table]

    def update(self, table, record_id, new_record):
        for i, rec in enumerate(self.data[table]):
            if rec["id"] == record_id:
                self.data[table][i] = new_record
                self.save()
                return True
        return False

    def delete(self, table, record_id):
        self.data[table] = [r for r in self.data[table] if r["id"] != record_id]
        self.save()


class Auth:
    def __init__(self, db):
        self.db = db

    def register(self):
        username = input("Username: ")
        password = input("Password: ")
        role = input("Role (admin/teacher/student): ")

        for user in self.db.get("users"):
            if user["username"] == username:
                print("User already exists!")
                return

        user = {
            "id": generate_id("USR"),
            "username": username,
            "password": hash_password(password),
            "role": role,
            "created_at": current_time()
        }

        self.db.add("users", user)
        print("Registration successful!")
        logging.info(f"New user registered: {username}")

    def login(self):
        username = input("Username: ")
        password = input("Password: ")

        for user in self.db.get("users"):
            if user["username"] == username and user["password"] == hash_password(password):
                print("Login successful!")
                logging.info(f"User logged in: {username}")
                return user

        print("Invalid credentials!")
        return None


class StudentManager:
    def __init__(self, db):
        self.db = db

    def add_student(self):
        name = input("Name: ")
        age = int(input("Age: "))
        dept = input("Department: ")

        student = {
            "id": generate_id("STU"),
            "name": name,
            "age": age,
            "department": dept,
            "created_at": current_time()
        }

        self.db.add("students", student)
        print("Student added successfully!")

    def view_students(self):
        students = self.db.get("students")
        if not students:
            print("No students found.")
            return

        for s in students:
            print(f"{s['id']} | {s['name']} | {s['department']}")

    def search_student(self):
        sid = input("Enter Student ID: ")
        for s in self.db.get("students"):
            if s["id"] == sid:
                print(s)
                return
        print("Student not found.")



class AttendanceManager:
    def __init__(self, db):
        self.db = db

    def mark_attendance(self):
        sid = input("Student ID: ")
        status = input("Present/Absent: ")

        record = {
            "id": generate_id("ATT"),
            "student_id": sid,
            "status": status,
            "date": current_time()
        }

        self.db.add("attendance", record)
        print("Attendance marked.")

    def view_attendance(self, sid):
        records = [r for r in self.db.get("attendance") if r["student_id"] == sid]

        if not records:
            print("No attendance records.")
            return

        for r in records:
            print(f"{r['date']} - {r['status']}")


class MarksManager:
    def __init__(self, db):
        self.db = db

    def add_marks(self):
        sid = input("Student ID: ")
        subject = input("Subject: ")
        marks = float(input("Marks: "))

        record = {
            "id": generate_id("MRK"),
            "student_id": sid,
            "subject": subject,
            "marks": marks
        }

        self.db.add("marks", record)
        print("Marks added.")

    def calculate_average(self, sid):
        marks = [m["marks"] for m in self.db.get("marks") if m["student_id"] == sid]
        if not marks:
            return 0
        return statistics.mean(marks)

    def calculate_grade(self, avg):
        if avg >= 90:
            return "A+"
        elif avg >= 75:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 40:
            return "C"
        else:
            return "Fail"


class Analytics:
    def __init__(self, db):
        self.db = db

    def top_student(self):
        students = self.db.get("students")
        if not students:
            print("No students.")
            return

        marks_manager = MarksManager(self.db)
        topper = None
        highest = 0

        for s in students:
            avg = marks_manager.calculate_average(s["id"])
            if avg > highest:
                highest = avg
                topper = s

        if topper:
            print(f"Topper: {topper['name']} with average {highest}")
        else:
            print("No marks data available.")


def admin_dashboard(db):
    sm = StudentManager(db)
    am = AttendanceManager(db)
    mm = MarksManager(db)
    an = Analytics(db)

    while True:
        print("\n--- ADMIN DASHBOARD ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Mark Attendance")
        print("4. Add Marks")
        print("5. Top Student")
        print("6. Logout")

        choice = input("Choice: ")

        if choice == "1":
            sm.add_student()
        elif choice == "2":
            sm.view_students()
        elif choice == "3":
            am.mark_attendance()
        elif choice == "4":
            mm.add_marks()
        elif choice == "5":
            an.top_student()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")


def main():
    db = Database()
    auth = Auth(db)

    while True:
        print("\n==== STUDENT MANAGEMENT SYSTEM ====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choice: ")

        if choice == "1":
            auth.register()
        elif choice == "2":
            user = auth.login()
            if user and user["role"] == "admin":
                admin_dashboard(db)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
