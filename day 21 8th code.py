with open("students.txt", "r") as f1:
    data = f1.read()

with open("backup.txt", "w") as f2:
    f2.write(data)

print("Backup created")
