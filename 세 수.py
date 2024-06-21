A, B, C = map(int, input().strip().split(' '))

if A <= B <= C or C <= B <= A:
    print(B)
elif B <= C <= A or A <= C <= B:
    print(C)
elif B <= A <= C or C <= A <= B:
    print(A)

