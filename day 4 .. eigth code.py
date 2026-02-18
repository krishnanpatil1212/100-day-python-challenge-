units = int(input("Enter electricity units:"))

if units<=100:
    bill=units*1.5
elif units<=200:
    bill=units*2.5
else:
    bill=unts*4

print(f"Total electricity bill:${bill}")
