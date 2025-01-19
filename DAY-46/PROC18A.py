for _ in range(int(input())):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    maxx = 0
    i = 0
    while i<n:
        maxx=max(maxx,sum(nums[i:i+k]))
        i+=1
    print(maxx)