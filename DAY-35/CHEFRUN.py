for _ in range(int(input())):
    x1, x2, x3, v1, v2 = map(int, input().split())
    
    # Calculate time taken by Chef and Kefa
    chef_time = abs(x3 - x1) / v1
    kefa_time = abs(x3 - x2) / v2
    
    # Determine the result
    if chef_time < kefa_time:
        print("Chef")
    elif chef_time > kefa_time:
        print("Kefa")
    else:
        print("Draw")
