bal = float(input("Enter balance: "))
wd = float(input("Enter withdrawal amount: "))

if(bal >= wd):
    bal -= wd;
    print(bal);
else:
    print("Withdrawal denied")