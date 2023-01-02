n = int(input("Enter N: "))

final = [];
for i in range(0,n):
    b = [];
    a = input("Enter command: ");
    b += a.split(" ");

    if(b[0] == "add"):
        final.append(b[1])
    elif(b[0] == "remove"):
        final.pop(int(b[1]));
    elif(b[0] == "print"):
        print(final)
