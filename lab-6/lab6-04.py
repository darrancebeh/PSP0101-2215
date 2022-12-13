n = int(input("Enter N: "))
total = 0;
for i in range(1,n+1):
    m = float(input(f"Enter Quiz Mark #{i}: "))
    total += m;

average = total/n;
print(f"Average = {average}")