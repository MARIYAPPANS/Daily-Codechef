t = int(input())
while t > 0:
    x = int(input())
    total_cost = 0
    current_value = 1
    for i in range(7):
        total_cost += current_value
        current_value *= 2
    if total_cost <= x:
        print("yes")
    else:
        print("no")
    t -= 1
