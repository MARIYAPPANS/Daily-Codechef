import sys

input = sys.stdin.read
data = input().split()
idx = 0
T = int(data[idx])
idx += 1
for _ in range(T):
    N = int(data[idx])
    idx += 1
    cnt = [0] * 10
    for _ in range(N):
        s = data[idx]
        idx += 1
        for j in range(10):
            if s[j] == '1':
                cnt[j] += 1
    res = 0
    for j in range(10):
        if cnt[j] % 2 == 1:
            res += 1
    print(res)