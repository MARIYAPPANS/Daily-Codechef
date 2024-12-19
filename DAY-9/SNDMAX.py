N = int(input())
for _ in range(N):
    numbers = list(map(int, input().split()))
    numbers.sort()
    print(numbers[1])
