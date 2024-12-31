t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    switches = 0
    current_gun = "close"  # Start with the close-range gun

    for distance in a:
        if distance > d and current_gun == "close":
            switches += 1
            current_gun = "long"
        elif distance <= d and current_gun == "long":
            switches += 1
            current_gun = "close"

    print(switches)
