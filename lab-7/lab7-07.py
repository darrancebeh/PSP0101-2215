p = float(input("Enter principal: RM"));
r = float(input("Enter interest rate, in %: "));
n = 10;

def ans(p, r):
    ans = round((p * (1 + (r/100))**n), 2)
    print(f"{n} years: RM{ans}");

while(n <= 60):
    ans(p, r);
    n += 10;