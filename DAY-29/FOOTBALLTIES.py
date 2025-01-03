t=int(input())
for _ in range(t):
    a,b=list(map(int,input().split()))
    s=min(a,b)
    print(s%3)
