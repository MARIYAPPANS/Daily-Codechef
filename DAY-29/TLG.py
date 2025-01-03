n = int(input())
max_lead, winner = 0, 0
cumulative1, cumulative2 = 0, 0

for _ in range(n):
    s1, s2 = map(int, input().split())
    cumulative1 += s1
    cumulative2 += s2
    lead = abs(cumulative1 - cumulative2)
    if lead > max_lead:
        max_lead = lead
        winner = 1 if cumulative1 > cumulative2 else 2

print(winner, max_lead)
