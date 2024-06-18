T = int(input().strip())

for _ in range(T):
    Mars = input().strip().split(' ')
    A = float(Mars[0])
    math = Mars[1:]

    for i in math:
        if i == '@':
            A *= 3
        elif i == '%':
            A += 5
        elif i == '#':
            A -= 7

    print("%.2f" % A)