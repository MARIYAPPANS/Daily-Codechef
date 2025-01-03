for _ in range(int(input())):
    n=int(input())
    if n>65:
        print("overload")
    elif n<35:
        print("underload")
    else:
        print("normal")