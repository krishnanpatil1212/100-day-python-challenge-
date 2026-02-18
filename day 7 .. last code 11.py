balance = 10000

while True:
    print("\nATM Menu")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Balance:", balance)

    elif choice == 2:
        amount = int(input("Enter amount: "))
        if amount <= balance:
            balance -= amount
            print("Withdraw successful")
        else:
            print("Insufficient balance")

    elif choice == 3:
        amount = int(input("Enter amount: "))
        balance += amount
        print("Deposit successful")

    elif choice == 4:
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")
