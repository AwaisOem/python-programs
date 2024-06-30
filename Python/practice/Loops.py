r = int(input("Enter number of rows:  "))

for i in range(r,1,-1):

    for k in range(1, r-i+1):
        if k == 1 or k == r-i:
            print("*", end="")
        else:
            print(" ", end="")
        pass
    for j in range(2, 2*i):
        print(" ", end="")
        pass
    for l in range(1, r-i+1):
        if l == 1 or l == r-i:
            print("*", end="")
        else:
            print(" ", end="")
        pass
    print("\n", end="")
    pass
for i in range(1,r+1):

    for k in range(1, r-i+1):
        if k == 1 or k == r-i:
            print("*", end="")
        else:
            print(" ", end="")
        pass
    for j in range(2, 2*i):
        print(" ", end="")
        pass
    for l in range(1, r-i+1):
        if l == 1 or l == r-i:
            print("*", end="")
        else:
            print(" ", end="")
        pass
    print("\n", end="")
    pass