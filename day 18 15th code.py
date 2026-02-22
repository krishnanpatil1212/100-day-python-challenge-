password = input("Enter password: ")

if len(password) >= 8 and password.isalnum():
    print("Strong password")
else:
    print("Weak password")
