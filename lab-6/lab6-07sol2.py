m = int(input("Enter M: "));
n = int(input("Enter N: "));

a = 0;

if(m > n):
    a = m;
else:
    a = n;
 
while(True):
    if(m % a == 0 and n % a == 0):
        ans = a;
        break;
    a -= 1;

print(f"Greatest common divisor = {ans}");