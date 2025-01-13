T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    count_1 = S.count('1')
    count_0 = N - count_1
    print(min(count_1, 1 + count_0))
