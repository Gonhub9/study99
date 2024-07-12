N = int(input().strip())

count_cute = 0
count_notcute = 0

for _ in range(N):
    cute = int(input().strip())

    if cute == 1:
        count_cute += 1
    elif cute == 0:
        count_notcute += 1

if count_cute < count_notcute:
    print('Junhee is not cute!')
elif count_cute > count_notcute:
    print('Junhee is cute!')
