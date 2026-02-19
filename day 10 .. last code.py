def add(a,b):
    return a+b

def substract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide (a,b):
    if b==0:
       return "cannot divide by zero"
    return a/b

print("calculator")
print("1.Add")
print("2.substract")
print("3.mutiply")
print("4.divide")

choice=int(input("Enter choice:"))
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))

if choice==1:
    print(add(x,y))

elif choice==2:
    print(substract(x,y))

elif choice==3:
    print(multiply(x,y))

elif choice==4:
    print(divide(x,y))

else:
    print("Invalid choice")
