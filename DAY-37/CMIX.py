T = int(input())
for _ in range(T):
    N = int(input())
    spells = [tuple(map(int, input().split())) for _ in range(N)]
    max_strength = 0
    for i in range(N):
        for j in range(i + 1, N):
            v1, a1 = spells[i]
            v2, a2 = spells[j]
            strength = a1 * v2 + v1 * a2
            max_strength = max(max_strength, strength)
    print(max_strength)
