balance = 5000

withdraw = int(input("Enter withdrawal amount: "))

if withdraw > 0:
    if withdraw <= balance:
        print("Withdrawal Successful")
    else:
        print("Insufficient Balance")
else:
    print("Invalid Amount")
    