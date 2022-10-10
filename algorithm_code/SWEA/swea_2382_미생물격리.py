import sys
sys.stdin = open('sample_input.txt', 'r')

def move():
    change = [[[] for _ in range(N)] for _ in range(N)]
    hive = list()

    for m in micro:
        if m[3] == 1:
            i, j = m[0] - 1, m[1]
        elif m[3] == 2:
            i, j = m[0] + 1, m[1]
        elif m[3] == 3:
            i, j = m[0], m[1] - 1
        elif m[3] == 4:
            i, j = m[0], m[1] + 1

        change[i][j].append([m[2], m[3]])

    for x in range(N):
        for y in range(N):
            if len(change[x][y]) >= 1:

                if len(change[x][y]) >= 2:
                    big, total, way = 0, 0, 0
                    for c in change[x][y]:
                        total += c[0]
                        if c[0] > big:
                            big = c[0]
                            way = c[1]
                    hive.append([x, y, total, way])

                elif x == 0:
                    hive.append([x, y, change[x][y][0][0] // 2, 2])
                elif x == N - 1:
                    hive.append([x, y, change[x][y][0][0] // 2, 1])
                elif y == 0:
                    hive.append([x, y, change[x][y][0][0] // 2, 4])
                elif y == N - 1:
                    hive.append([x, y, change[x][y][0][0] // 2, 3])

                else:
                    hive.append([x, y, change[x][y][0][0], change[x][y][0][1]])

    return hive


T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    micro = [list(map(int, input().split())) for _ in range(K)]
    arr = [[0] * N for _ in range(N)]
    answer = 0

    for m in range(M):
        micro = move()
    
    for m in micro:
        answer += m[2]

    print('#{} {}'.format(tc, answer))