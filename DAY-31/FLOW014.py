for _ in range(int(input())):
    h, c, t = map(float, input().split())
    print(10 if h > 50 and c < 0.7 and t > 5600 else
          9 if h > 50 and c < 0.7 else
          8 if c < 0.7 and t > 5600 else
          7 if h > 50 and t > 5600 else
          6 if h > 50 or c < 0.7 or t > 5600 else
          5)
