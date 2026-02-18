bill=int(input("Enter total bill amount:"))
member=input("Are you member?(yes/no):")

if bill>=5000:
    if member=="yes":
        discount=bill*0.20
        print("20% discount applied")
    else:
        discount=bill*0.10
        print("10% discount applied")

    print("discount amount:",discount)
    print("final bill:",bill-discount)
else:
    print("no discount available")
    print("final bill:",bill)
