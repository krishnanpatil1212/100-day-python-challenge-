username = input("username:")
password = input("password:")

if username =="admin":
    if password=="1234":
        print("login successful")
    else:
        print("wrong password")
else:
    print("username not found")
