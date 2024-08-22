while True:
    N = int(input().strip())

    if N == -1:
        break

    LIST = []
    ALL = 0

    for i in range(1, N // 2 + 1):
        if N % i == 0:
            LIST.append(i)
            ALL += i

    if ALL == N:
        LIST_str = " + ".join(map(str, LIST))
        print(f"{N} = {LIST_str}")

    else:
        print(f"{N} is NOT perfect.")
