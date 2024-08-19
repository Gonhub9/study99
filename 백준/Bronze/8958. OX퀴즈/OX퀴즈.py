T = int(input().strip())

for _ in range(T):
    OX = input().strip()
    score = 0
    real_score = 0

    for OX in OX:
        if OX == 'O':
            real_score += 1
            score += real_score

        else:
            real_score = 0

    print(score)
