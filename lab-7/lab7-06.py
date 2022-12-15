n = int(input("Enter N: "))
lc = 0;
m = 0;
total = round(n/2, 0);

for i in range(lc, n):
    line = "";
    sc = n - lc;
    lc += 1;
    line += sc*(" ");
    line += lc*("*");
    line += (lc-1)*("*");

    if(lc >= total+1):
        break;
    print(line);
