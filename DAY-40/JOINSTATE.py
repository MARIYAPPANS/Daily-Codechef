T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    
    count, current_sum = 0, 0
    for value in A:
        current_sum += value
        if current_sum >= M:
            count += 1
            current_sum = 0
    
    print(count)
