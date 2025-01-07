for _ in range(int(input())):
    k=int(input())
    s=0
    for i in range(1,k+1):
        if i%2!=0:
            s+=3
        else:
            s-=1
    print(s)