balance = 10000

while True:
    print("\nATM Menu")
    print("1.check balance")
    print("2.withdraw")
    print("3.deposit")
    print("4.Exit")

    choice = int(input("Enter choice:"))

    if choice == 1:
        print("Balance:", balance)
        
    elif choice==2:
        amount=int(input("Enter amount:"))
        if amount<=balance:
            balance-=amount
            print("withdraw successful")
        else:
            print("insufficient balance")
            
    elif choice==3:
        amount=int(input("Enter amount:"))
        balance+=amount
        print("deposit successful")
        
    elif choice==4:
        print("thank ypu for using ATM")
        break
    
    else:
        print("invalid choice")

