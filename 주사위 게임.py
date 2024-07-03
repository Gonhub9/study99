T = int(input().strip())

results = []

for _ in range(T):
    A, B, C = map(int, input().strip().split())

    if A == B == C:
        money = (10000 + (A * 1000))
    elif A == B or A == C:
        money = (1000 + A * 100)
    elif B == C:
        money = (1000 + B * 100)
    elif A != B != C:
        money = (max(A, B, C) * 100)

    results.append(money)

print(max(results))
