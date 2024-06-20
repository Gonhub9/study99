A = int(input().strip())
B = input().strip()
C = int(input().strip())

result = 0

if B[0] == '+':
    result = A + C
if B[0] == '*':
    result = A * C

print(result)