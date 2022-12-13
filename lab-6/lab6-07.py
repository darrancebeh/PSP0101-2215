m = int(input("Enter M: "))
n = int(input("Enter N: "))

md = [];
nd = [];
ans = [];

for i in range(1, m+1):
    if(m % i == 0):
        md.append(i);

for j in range(1, n+1):
    if(n % j == 0):
        nd.append(j);

for div in md:
    for div2 in nd:
        if(div2 == div):
            ans.append(div2);

temp = 0;

for a in ans:
    if(a > temp):
        temp = a;

print(f"Greatest common divisor = {temp}");