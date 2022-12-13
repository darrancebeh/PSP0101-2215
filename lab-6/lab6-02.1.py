n = int(input("Enter N: "));

ans = "";

i = 1;
while(i <= n):
    if(i % 2 == 0):
        ans += (str(i) + ", ");
    i += 1;  

print(ans[:-2])