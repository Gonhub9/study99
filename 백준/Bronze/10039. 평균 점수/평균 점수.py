A = int(input().strip())
B = int(input().strip())
C = int(input().strip())
D = int(input().strip())
E = int(input().strip())

result = 0

if A < 40:
    A = 40
if B < 40:
    B = 40
if C < 40:
    C = 40
if D < 40:
    D = 40
if E < 40:
    E = 40

result = (A + B + C + D + E)
print(result // 5)