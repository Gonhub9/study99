# K는 과자 한 개의 가격, 사려는 과자의 개수 N, 가진 돈 M

# 과자 한 개의 가격은 30원이다. 사려고 하는 과자의 개수는 4개. 현재 동수가 가진 돈은 100원 그럼 받아야 하는 돈은 20원

K, N, M = map(int, input().strip().split(' '))

if K * N > M:
    print(K * N - M)
elif K * N <= M:
    print(0)