# cook your dish here
t=int(input())
for a in range(t):
    n,k,x = map(int,input().split())
    p = 2**(k-1)
    if(p <= x):
        print("Yes")
    else:
        print("No")