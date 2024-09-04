T = int(input().strip())

for _ in range(T):
    T_CASE = int(input().strip())
    alc = -1
    drink = ""

    for _ in range(T_CASE):
        A, B = input().strip().split(' ')
        B = int(B)

        if B > alc:
            alc = B
            drink = A

    print(drink)