import math
print("=======SCIENTIFIC TEMPERATURE TOOL=========")
print("1. celsius to fahrenheit")
print("2. fahrenheit to celsius")
print("3. square root of temperatire")
print("4. Round temperature")

choice = int(input("Enter your choice:"))

if choice==1:
    c=float(input("Enter celsius:"))
    f=(c*9/5)+32
    print(f"{c}c={f:.2f}f")

elif choice==2:
    f=float(input("Enter fahrenheit:"))
    c=(f-32)*5/9
    print(f"{f}c={c:.2f}c")

elif choice==3:
    t=float(input("Enter temperature:"))
    print(f"sruare root={math.sqrt(t):.2f}")

elif choice==4:
    t=float(input("Enter temperature:"))
    print("ceil:",math.ceil(t))
    print("floor:",math.floor(t))

else:
    print("invalid choice")
