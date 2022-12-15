def isPrime(n):
    a = 2;
    while(a < n-1):
        if(n % a == 0):
            return False;
        a += 1;
    return True;

n = int(input("Enter N: "));

if(isPrime(n)):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is NOT a prime number.")