b = [];
bInt = [];
a = input("Enter scores: ");
b += a.split(" ");

for i in b:
    if int(i) not in bInt:
        bInt.append(int(i))

bInt.sort();
print(f"Second smallest score = {bInt[1]}")