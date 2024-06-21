N = int(input().strip())

S = 2

while N > 1:
    while N % S == 0:
        print(S)
        N //= S
    S += 1
