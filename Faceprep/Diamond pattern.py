
n=int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()
for i in range(n-1,-1,-1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()

     
 