price = float(input("Enter item price: "))
tag = input("Enter tag colour: ").lower()

d = {
    "white" : 100/100,
    "yellow" : 75/100,
    "red" : 50/100,
    "blue": 30/100
}

totaldisc = 0;

aeon = input("Do you have a member card? (y/n): ").lower()[0];
if(aeon == 'y'):
    price = (price * (d[tag]- 5/100))
    totaldisc -= 0.05
else:
    price = (price * d[tag]);

totaldisc += d[tag]; 
totaldisc *= 100;
totaldisc -= 100;
totaldisc = abs(totaldisc);

print(f"Total discount = {totaldisc} %");
print(f"Final price = RM{price}");