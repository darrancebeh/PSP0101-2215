n = int(input("Enter N: "));
listP = [];
listQ = [];
pInt = [];
qInt = [];
p = input("Enter list P: ");
q = input("Enter list Q: ");

listP += p.split(",")
listQ += q.split(",")

for p in listP:
    pInt.append(int(p));
for q in listQ:
    qInt.append(int(q));

for i in pInt:
    for j in qInt:
        if(i + j == n):
            print(f"({i}, {j})")