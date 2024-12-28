T = int(input())
for _ in range(T):
    A, B, X, Y = map(int, input().split())
    time_chef = A / X
    time_chefina = B / Y
    if time_chef < time_chefina:
        print("Chef")
    elif time_chefina < time_chef:
        print("Chefina")
    else:
        print("Both")
