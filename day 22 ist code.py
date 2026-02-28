try:
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    print("Result:", a / b)

except ZeroDivisionError:
    print("❌ Cannot divide by zero")

except ValueError:
    print("❌ Please enter numbers only")

print("Program continues...")
