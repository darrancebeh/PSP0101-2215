n = int(input("Enter N: "))
ans = "";

for i in range(1, n+1):
    if n % i == 0:
        ans += (str(i) + ", ");

print(ans[:-2]);