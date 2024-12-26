t = int(input())
while t > 0:
    n, k, m = map(int, input().split())
    max_candies_per_bag = k * m
    bags_required = (n + max_candies_per_bag - 1) // max_candies_per_bag  # This is a shortcut for ceiling division
    print(bags_required)
    t -= 1



