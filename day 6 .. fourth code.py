attendence=int(input("Enter your attendence persentage:"))
fee_paid=input("fee paid?(yes/no):")

if attendence>=75:
    if fee_paid=="yes":
        print("you are allowed to write exam")
    else:
        print("clear the fee first")
else:
    print("attendence it too low")
