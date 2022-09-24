from collections import deque
import sys

input = sys.stdin.readline

N, L, R = map(int, input().split())

country = [list(map(int, input().split())) for _ in range(N)]

move = 0

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

while True:
    visited_list = [[0] * N for _ in range(N)]
    true = 0

    for x in range(N):
        for y in range(N):
            if visited_list[x][y] == 0:
                queue = deque([(x, y)])
                visited_list[x][y] = 1

            # print(queue)
            search = [(x, y)]
            while queue:
                # print(queue)
                i, j = queue.pop()
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < N and 0 <= nj < N and visited_list[ni][nj] == 0:
                        if L <= abs(country[i][j] - country[ni][nj]) <= R:
                            queue.appendleft((ni, nj))
                            visited_list[ni][nj] = 1
                            search.append((ni, nj))
            # print(search)
            if len(search) > 1:
                true = -1
                total = 0
                for i, j in search:
                    total += country[i][j]
                mean = total // len(search)
                for i, j in search:
                    country[i][j] = mean

    if true == 0:
        break
    else:
        move += 1

print(move)

