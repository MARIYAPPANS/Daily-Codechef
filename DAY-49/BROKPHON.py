import sys

input = sys.stdin.read
data = input().split()
idx = 0
T = int(data[idx])
idx += 1
for _ in range(T):
    N = int(data[idx])
    idx += 1
    A = list(map(int, data[idx:idx + N]))
    idx += N
    c = 0
    for i in range(N):
        if (i == 0 and A[i] != A[i + 1]) or \
           (i == N - 1 and A[i] != A[i - 1]) or \
           (0 < i < N - 1 and (A[i] != A[i - 1] or A[i] != A[i + 1])):
            c += 1
    print(c)