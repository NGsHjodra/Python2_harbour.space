n = int(input("Enter num: "))
while (n!=0):
    if n > 0:
        for i in range(0,n):
            print(i+1,end=" ")
    else:
        for i in range(0,n,-1):
            print(i-1,end=" ")
    print()
    n = int(input("Enter num: "))
print("Buy!!")