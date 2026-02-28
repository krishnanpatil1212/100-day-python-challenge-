try:
    balance = 5000
    amount = int(input("Enter amount: "))

    if amount > balance:
        raise ValueError("Insufficient balance")

    print("Please collect cash")

except ValueError as e:
    print("❌ Error:", e)

finally:
    print("Thank you for using ATM")
