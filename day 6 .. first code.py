age =int(input("Enter your age:"))
citizen = True

if age>=18:
    if citizen:
        print("Eligible to vote")
    else:
        print("must be citizen")
else:
    print("underage")
