from collections import Counter

T = int(input())

for t in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    D = list(map(int, input().split()))
    C = Counter(A+D)
    print(max(C.values()))
    
    
    