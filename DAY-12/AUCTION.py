# cook your dish here
# cook your dish here
t=int(input())
while(t):
    x,y,z=map(int,input().split())
    if max(max(x,y),z)==x:
        print("alice")
    elif max(max(x,y),z)==y:
        print("bob")
    else:
        print("charlie")
    t=t-1