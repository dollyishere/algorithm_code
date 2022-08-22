T = int(input())

for t in range(T):
    N = int(input())
    snail = [[0] * N for _ in range(N)]

    trigger = 1
    num = 1
    x = 0
    y = 0
    ran = N
    for n in range(2 * N - 1):
        if n % 2 == 0:
            for i in range(ran):
                snail[x][y] = num
                num += 1
                if i == ran - 1:
                    pass
                else:
                    y += (1 * trigger)
            ran -= 1
            x += (1 * trigger)
        elif n % 2:
            for i in range(ran):
                snail[x][y] = num
                num += 1
                if i == ran - 1:
                    pass
                else:
                    x += (1 * trigger)
            trigger = -1 * trigger
            y += (1 * trigger)


    print('#{}'.format(t + 1))
    for i in range(N):
        for j in range(N):
            if j == N - 1:
                print(snail[i][j])
            else:
                print(snail[i][j], end=' ')


