a = input("Enter a sentence: ");
ind = 0;
fw = "";
lw = "";

b = a.split(" ");
fw = b[0];
lw = b[len(b) - 1]

print(f"First word: {fw}")
print(f"Last word: {lw}")