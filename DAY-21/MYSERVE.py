t = int(input())  # Number of test cases
while t > 0:
    p, q = map(int, input().split())  # Scores of Alice and Bob
    total_serves = p + q  # Total number of serves
    # Check if the serve number falls in Alice's or Bob's turn
    if (total_serves // 2) % 2 == 0:
        print("Alice")
    else:
        print("Bob")
    t -= 1
