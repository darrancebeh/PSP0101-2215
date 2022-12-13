n = int(input("Enter N: "))

ans = "";

for i in range(1, n+1):
    ans += (str(n) + ", ");
    n -= 1;

print(ans[:-2]);