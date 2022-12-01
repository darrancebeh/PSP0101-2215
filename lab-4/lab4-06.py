n1 = int(input("Enter numerator #1: "))
d1 = int(input("Enter denominator #1: "))

n2 = int(input("Enter numerator #2: "))
d2 = int(input("Enter denominator #2: "))

n = (n1*d2) + (n2*d1)
d = d1*d2

print(f"{n1}/{d1} + {n2}/{d2} = {n}/{d}")