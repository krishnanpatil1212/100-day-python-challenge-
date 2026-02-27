username = input("Enter username: ")
password = input("Enter password: ")

with open("users.txt", "a") as file:
    file.write(username + "," + password + "\n")

print("User registered successfully")
