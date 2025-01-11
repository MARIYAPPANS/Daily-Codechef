def can_reach_code_town(S):
    vowels = {'A', 'E', 'I', 'O', 'U'}
    target = 'CODETOWN'
    
    for i in range(8):
        if S[i] in vowels and target[i] not in vowels:
            return "NO"
        if S[i] not in vowels and target[i] in vowels:
            return "NO"
    return "YES"

T = int(input())
for _ in range(T):
    S = input().strip()
    print(can_reach_code_town(S))
