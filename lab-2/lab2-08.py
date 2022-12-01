a = int(input("Input a year: \n"))

if(a % 4 != 0):
    print("Common year")
else:
    if(a % 100 != 0):
        print("Leap year")
    elif(a % 400 != 0):
        print("Common year")
    else:
        print("Leap year")