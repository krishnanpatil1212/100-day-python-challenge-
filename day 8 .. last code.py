print("DAY 8 - BIG PRACTICE PROGRAM")
print("----------------------------")

print("\n1) printing numbers 1 to 10(skip5)")

for i in range (1,11):
    if i==5:
        continue
    print(i)

print("\n2) printing numbers until7")

for i in range (1,11):
    if i>7:
        break
    print(i)

print("\n3) checking numbers(pass example)")

for i in range (1,6):
    if i == 3:
        pass
    else:
        print("number:",i)

print("\n program finished")
