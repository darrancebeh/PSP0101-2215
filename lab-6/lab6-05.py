n = int(input("Enter N: "));
temp = 0.00;

for i in range(1, n+1):
    num = float(input(f"Enter number #{i}: "))
    if(num > temp):
        temp = num;

print(f"{temp} is the largest.")