t=int(input())
while(t):
    x,y,z=map(int,input().split())
    if (max(max(x,y),z))==x:
        print("Setter")
    elif (max(max(x,y),z))==y:
        print("Tester")
    else:
        print("Editorialist")
    t=t-1