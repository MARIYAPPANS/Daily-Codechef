# cook your dish here
t=int(input())
while(t):
    x,n=map(int,input().split())
    print((x//10)*n)
    t=t-1