H, M = map(int, input().strip().split(' '))

if M < 45:
    H = H - 1
    M = M + 60 - 45
else:
    M = M - 45

if H < 0:
    H = 23

print(H, M)
