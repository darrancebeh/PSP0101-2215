a = input("Enter a sentence: ").lower();
v = ['a', 'e', 'i', 'o', 'u'];
ans = 0;

for i in a:
    if(i in v):
        ans += 1;
print(f"Number of vowels = {ans}")