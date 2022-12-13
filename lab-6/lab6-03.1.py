n = int(input("Enter N : "))

ans = "";

i = 1;
while(n >= i):
    ans += (str(n) + ", ");
    n -= 1;

print(ans[:-2]);