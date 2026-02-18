temp=float(input("Enter temperature value:"))
unit=input("Enter unit(c or f):")

if unit=="c":
    f=(temp*9/5)+32
    print(f"{temp}c={f:.2f}c")

elif unit=="f":
    c=(temp-32)*5/9
    print(f"{temp}f={c:.2f}f")

else:
    print("invalid unit")
