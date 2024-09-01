T = int(input().strip())

A = 300
B = 60
C = 10

if T % C != 0:
    print(-1)

else:
    print_A = T // A
    T %= A

    print_B = T // B
    T %= B

    print_C = T // C
    T %= C

    print(print_A, print_B, print_C)
