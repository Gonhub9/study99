people = input().strip()
winner = input().strip()

count_A = winner.count('A')
count_B = winner.count('B')

if count_A > count_B:
    print('A')

elif count_B > count_A:
    print('B')

elif count_B == count_A:
    print('Tie')
