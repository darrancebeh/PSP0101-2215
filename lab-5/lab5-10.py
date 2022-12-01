p = int(input("Enter your package number:\n"))
m = int(input("Enter your minutes spent: \n"))

if(p == 3):
    payment = 70;
else:
    if(p == 2):
        if(m <= 900):
            payment = 60;
        else:
            m -= 900;
            payment = 60 + (m * 0.4);
    if(p == 1):
        if(m <= 450):
            payment = 40;
        else:
            m -= 450;
            payment = 40 + (m*0.45)

print(payment)