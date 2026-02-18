balance = 5000
withdraw=int(input("Enter amount to withdraw:"))

if withdraw<=balance and withdraw %100==0:
    print("please collect your money")
else:
    print("Invalid ammount or insufficient balance")
