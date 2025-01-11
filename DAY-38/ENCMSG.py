for _ in range(int(input())):
    n = int(input())
    s = list(input())
    
    # Step 1: Swap characters in pairs
    for i in range(0, n - 1, 2):
        s[i], s[i + 1] = s[i + 1], s[i]
    
    # Step 2: Replace characters with their reverse counterparts
    encoded = ''.join(chr(219 - ord(c)) for c in s)  # 219 = 'a' + 'z'
    print(encoded)
