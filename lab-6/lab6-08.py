m = int(input("Enter m: "))
n = int(input("Enter n: "))
a = 0;

if(m > n):
    a = m;
else:
    a = n;

while(True):
    if(a % m == 0 and a % n == 0):
        ans = a;
        break;
    a += 1;

print(f"Least common multiplier = {a}")