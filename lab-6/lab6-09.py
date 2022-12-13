def isPrime(n):
    a = 2;
    while(a < n-1):
        if(n % a == 0):
            return (f"{n} is NOT a prime number.");
    return (f"{n} is a prime number.");

n = int(input("Enter N: "));

print(isPrime(n));