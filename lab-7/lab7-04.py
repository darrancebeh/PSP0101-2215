a = input("Enter a word: ");
b = a.lower();
c = b[::-1];

if b == c:
    print(f"{a} is a palindrome.")
else:
    print(f"{a} is NOT a palindrome.")