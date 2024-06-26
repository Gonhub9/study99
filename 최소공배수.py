import math

T = int(input().strip())

for _ in range(T):
    A, B = map(int, input().strip().split(' '))
    print(math.lcm(A, B))