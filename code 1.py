# ===============================
# DAY 1–2: Print, Variables, Data Types, Boolean
# ===============================

print("Welcome to Python Learning System")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
is_student = True

print(f"Hello {name}, Age: {age}, Student: {is_student}")


# ===============================
# DAY 3: f-strings
# ===============================

print(f"{name}, you will be {age + 1} next year.")


# ===============================
# DAY 4: Input, Operators
# ===============================

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum:", num1 + num2)


# ===============================
# DAY 5: Type Conversion & math module
# ===============================

import math

print("Square root of num1:", math.sqrt(num1))
print("Ceil of num2:", math.ceil(num2))


# ===============================
# DAY 6: if–else, nested if
# ===============================

if age >= 18:
    has_license = input("Do you have a license? (yes/no): ")
    if has_license == "yes":
        print("You are allowed to drive")
    else:
        print("Get a license first")
else:
    print("You are under 18, driving not allowed")


# ===============================
# DAY 7: Loops (for, while)
# ===============================

print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)

count = 1
while count <= 3:
    print("While loop count:", count)
    count += 1


# ===============================
# DAY 8: break, continue
# ===============================

for i in range(1, 6):
    if i == 3:
        continue
    if i == 5:
        break
    print("Loop value:", i)


# ===============================
# DAY 9: Pattern
# ===============================

print("Heart Pattern:")
print(" ❤️❤️   ❤️❤️ ")
print("❤️❤️❤️❤️❤️❤️")
print(" ❤️❤️❤️❤️ ")
print("   ❤️❤️ ")


# ===============================
# DAY 10: Functions
# ===============================

def greet(user):
    return f"Welcome, {user}!"

print(greet(name))


# ===============================
# DAY 11: lambda, map, filter, reduce
# ===============================

from functools import reduce

numbers = [1, 2, 3, 4, 5]

doubled = list(map(lambda x: x * 2, numbers))
even = list(filter(lambda x: x % 2 == 0, doubled))
total = reduce(lambda a, b: a + b, even)

print("Doubled:", doubled)
print("Even:", even)
print("Total:", total)


# ===============================
# DAY 12: Recursion
# ===============================

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))


# ===============================
# DAY 13: Lists
# ===============================

marks = [78, 85, 90]
marks.append(88)
print("Marks:", marks)


# ===============================
# DAY 14: Tuples
# ===============================

student_info = ("Krishna", 21, "India")
name_t, age_t, country_t = student_info
print(name_t, age_t, country_t)


# ===============================
# DAY 15: Sets
# ===============================

emails = ["a@gmail.com", "b@gmail.com", "a@gmail.com"]
unique_emails = set(emails)
print("Unique emails:", unique_emails)


# ===============================
# DAY 16: Dictionary
# ===============================

student = {
    "name": name,
    "age": age,
    "marks": marks
}

print("Student Record:")
for key, value in student.items():
    print(key, ":", value)


# ===============================
# DAY 17: Strings (slicing, methods)
# ===============================

message = "  python is powerful  "
print(message.strip().title())
print("Reversed name:", name[::-1])

print("Program Finished Successfully 🎉")
