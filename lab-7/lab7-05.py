n = int(input("Enter N: "))
lc = 0;
for i in range(lc, n):
    line = "";
    sc = n - lc;
    lc += 1;
    line += sc*(" ")
    line += lc*("*")
    print(line)