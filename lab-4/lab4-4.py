g = int(input("Enter the weight in grams: "))
kg = 0

while(g >= 1000):
    kg += 1;
    g -= 1000;

print(f"{g} grams = {kg} kilograms and {g} grams")