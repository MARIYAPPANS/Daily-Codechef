# https://www.codechef.com/problems/ASSIGNMNT

t=int(input())
while(t):
    x,y,z=map(int,input().split())
    if x*y<=z*24*60:
        print("yes")
    else:
        print("no")
    t=t-1