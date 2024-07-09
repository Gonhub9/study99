T = int(input().strip())

for _ in range(T):
    R, E, C = map(int, input().strip().split(' '))

    if R < E - C:
        print('advertise')

    elif R > E - C:
        print('do not advertise')

    elif R == E - C:
        print('does not matter')
