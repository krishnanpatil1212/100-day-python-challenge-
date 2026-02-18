word = "Krishna"

with open("students.txt", "r") as file:
    content = file.read()

if word in content:
    print("Word found")
else:
    print("Word not found")
