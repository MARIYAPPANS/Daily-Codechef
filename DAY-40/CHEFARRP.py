T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        sum_val = 0
        product_val = 1
        for j in range(i, N):
            sum_val += A[j]
            product_val *= A[j]
            if sum_val == product_val:
                count += 1
    print(count)
