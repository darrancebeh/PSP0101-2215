print("A - Rectangle\nB - Triangle\nC - Circle");

s = input("Enter shape: ").lower()[0]

if(s == 'a' or s =='b'):
    h = int(input("Enter height: "))
    b = int(input("Enter base: "))
elif(s == 'c'):
    r = int(input("Enter radius: "))

if(s == 'a'):
    area = (h*b)
elif(s == 'b'):
    area = (h*b)/2
elif(s == 'c'):
    area = 22/7 * r * r;

print(f"Area = {area}")