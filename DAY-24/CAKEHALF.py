import math

def eat_slices(A, B):
    if A == B:  # Base case: If both have the same slices, no one is unhappy
        return 0
    if A > B:  # If Alice has more slices
        eaten = math.ceil(A / 2)
        return eaten + eat_slices(A - eaten, B)
    else:  # If Bob has more slices
        eaten = math.ceil(B / 2)
        return eaten + eat_slices(A, B - eaten)

t = int(input())
for _ in range(t):
    A, B = map(int, input().split())
    print(eat_slices(A, B))
