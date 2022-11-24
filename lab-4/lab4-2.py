hour = int(input("Enter hours: "))
mins = int(input("Enter minutes: "))

while(mins >= 60):
    mins -= 60
    hour += 1

print(f"Time is {hour}:{mins}")