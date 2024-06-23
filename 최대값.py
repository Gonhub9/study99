S = int(input().strip())
N = 0
O = 1
count = 0

while N + O <= S:
    N += O
    count += 1
    O += 1

print(count)
