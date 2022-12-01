hours = int(input("Input your hours:"))
payment = 0
if(hours == 1):
    payment = 2.5
else:
    if(hours == 2):
        payment = 2.5 + 1.5
    else:
        payment = 4 + (hours * 2)

print(hours)