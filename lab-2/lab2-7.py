hours = int(input("Hours worked: \n"))
payment = 0;

for i in range(0, hours):
    if(i < 40):
        payment += 25
    else:
        payment += 50

print(payment)