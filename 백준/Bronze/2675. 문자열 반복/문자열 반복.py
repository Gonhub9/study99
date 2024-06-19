S = int(input().strip())
T2 = 0

for _ in range(S):
    TRY, STR = input().strip().split(' ')
    T = int(TRY)
    result = ""

    for i in STR:
        result += i * T

    print(result)