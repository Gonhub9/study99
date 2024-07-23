while True:
    A, B = map(int, input().strip().split(' '))
    if A == 0 and B == 0:
        break

    if B % A == 0:
        print('factor')

    if A % B == 0:
        print('multiple')

    if A % B and B % A != 0:
        print('neither')
