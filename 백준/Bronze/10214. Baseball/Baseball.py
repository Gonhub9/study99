T = int(input().strip())

for _ in range(T):
    Y = K = 0

    for _ in range(9):
        A, B = map(int, input().split())
        Y += A
        K += B

    if Y > K:
        print('Yonsei')
    elif Y < K:
        print('Korea')
    else:
        print('Draw')
