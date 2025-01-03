t=int(input())
for _ in range(t):
    a=list(map(int,input().split()))
    s=a[0:3]
    p=a[3:]
    q=sorted(s)
    r=sorted(p)
    
    m=q[-1]+q[-2]
    n=r[-1]+r[-2]
    
    if m>n:
        print("alice")
    elif m<n:
        print("bob")
    else:
        print("tie")
