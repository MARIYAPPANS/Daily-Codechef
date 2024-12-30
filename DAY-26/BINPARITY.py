t = int(input())
for _ in range(t):
    m = int(input())
    summ = bin(m).count('1')
    print("even" if summ % 2 == 0 else "odd")
