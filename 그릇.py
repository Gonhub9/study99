A = input().strip()

result = 10

for i in range(1, len(A)):
    if A[i] == A[i-1]:
        result += 5
    else:
        result += 10

print(result)
