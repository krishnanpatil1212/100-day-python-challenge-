

print("temperature converter")
print("1.celsius to fahrenheit")
print("2.fahrenheit to celsius")

choice = int(input("Enter your choice(1or2):"))

if choice==1:
    celsius=float(input("Enter temperature in celsius:"))
    fahrenheit=(celsius*9/5)+32
    print(f"{celsius}c={fahrenheit:.2f}f")

elif choice==2:
    fahrenheit=float(input("Enter temperature in fahrenheit:"))
    celsius=(fahrenheit-32)*5/9
    print(f"{fahrenheit}f={celsius:.2f}c")

else:
    print("invalid choice")
