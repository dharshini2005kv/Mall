Amount = 10000
print("Welcome to Deva Bank!")

while True:
    print("Choose 1 to show balance")
    print("Choose 2 to Withdraw")
    print("Choose 3 to Deposite")
    print("Choose 4 to Exit")
    
    a = int(input("Enter: "))

    if a == 1:
        print("Balance : ", Amount)
    elif a == 2:
        b = int(input("Enter Amount: "))
        if b <= Amount and b>0:
            Amount = Amount-b
            

            print("Withdrawal successful")
            print("Remaining balance: ", Amount)
        else:
            print("Insufficient Amount")

        
    elif a == 3:
        c = int(input("Deposit Amount: "))
        Amount = Amount+c
        print("Amount : ", Amount)
        
    elif a ==4:
        break
    else:
        print("Invalid")
