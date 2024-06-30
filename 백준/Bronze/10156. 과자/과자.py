K, N, M = map(int, input().strip().split(' '))

if K * N > M:
    print(K * N - M)
elif K * N <= M:
    print(0)