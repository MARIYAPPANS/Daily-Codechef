t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    count, total_calories = 0, 0
    for calorie in a:
        if total_calories + calorie > k:
            break
        total_calories += calorie
        count += 1
    print(count)
