t=int(input())
while(t>0):
    x,y,z=map(int,input().split())
    one_g=2*((x*y)+(y*z)+(z*x))
    print(1000//one_g)
    t-=1