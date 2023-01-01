a = input("Enter a sentence: ");
b = a.split(" ");

print(f"Number of words: {len(b)}");
print(f"First word: {b[0]}");
print(f"Last word: {b[len(b)-1]}");