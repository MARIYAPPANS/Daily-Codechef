t=int(input())
for _ in range(t):
    n=int(input())
    m=list(map(int,input().split()))
    print(sum(m)-min(m))