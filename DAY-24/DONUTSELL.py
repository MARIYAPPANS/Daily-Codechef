t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    donuts = list(map(int, input().split()))
    requests = list(map(int, input().split()))
    sad_customers = 0
    for request in requests:
        if donuts[request - 1] > 0:
            donuts[request - 1] -= 1
        else:
            sad_customers += 1
    print(sad_customers)
