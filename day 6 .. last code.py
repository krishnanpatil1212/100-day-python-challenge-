charge=input("put on charge:")
password=input("password?(correct/wrong):")

if charge>="80":
    if password=="correct":
       print("charged")
    else:
        print("charging")
else:
    print("wrong password")
    
