d1 = float(input("Price of drink #1: RM"))
d2 = float(input("Price of drink #2: RM"))

if(d1 > d2):
    d2 *= 50/100;
else:
    d1 *= 50/100;

d3 = d1 + d2;
print(f"Total price =  RM{d3}")