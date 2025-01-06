t = int(input())
while t > 0:
    x,y,z,m= map(int, input().split())
    s=z//x 
    d=m//y 
    print(s+d)
    t -= 1

