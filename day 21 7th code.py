with open("users.txt", "r") as file:
    users = file.readlines()

for user in users:
    print(user.strip())
