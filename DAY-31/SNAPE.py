for _ in range(int(input())):
    B, LS = map(int, input().split())
    min_RS = (LS**2 - B**2)**0.5
    max_RS = (LS**2 + B**2)**0.5
    print(f"{min_RS:.5f} {max_RS:.5f}")
