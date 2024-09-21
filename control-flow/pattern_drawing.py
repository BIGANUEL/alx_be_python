user = int(input("Enter the size of the pattern: "))
i =1
while i<= user:
    for j in range (user):
        print("*",end="")
    i+=1
    if i == user:
        break
    print()