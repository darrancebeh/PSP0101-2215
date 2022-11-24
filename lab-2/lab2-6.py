n1 = int(input("Input your first number: \n"))
n2 = int(input("Input your second number: \n"))
n3 = int(input("Input your third number: \n"))

if(n1 > n2 and n1 > n3):
    print(n1)
elif(n2 > n1 and n2 > n3):
    print(n2)
else:
    print(n3)