import sys
sys.stdin = open('sample_input(1).txt', 'r')


def len_1(arr):
    cnt = 0
    for a in arr:
        cnt += 1
    return cnt

def change(c, color):
    global arr
    for a in c:
        i, j = a[0], a[1]
        arr[i][j] = color

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    black = 0
    white = 0

    # 판에 먼저 지시한대로 돌 배치한 후에 시작
    num = N // 2 - 1
    arr[num][num], arr[num+1][num+1] = 2, 2
    arr[num][num+1], arr[num+1][num] = 1, 1

    # 가로 세로
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    # 대각선
    dx = [1, 1, -1, -1]
    dy = [1, -1, 1, -1]

    for m in range(M):
        x, y, stone_c = map(int, input().split())
        x -= 1
        y -= 1
        arr[x][y] = stone_c
        change_stones = list()

        arr_2 = [[0] * N for _ in range(N)]
        print('기준점', x, y)
        print(arr)
        for k in range(4):
            check = list()
            for n in range(1, N):
                ni = x + (di[k] * n)
                nj = y + (dj[k] * n)
                if 0 <= ni < N and 0 <= nj < N:
                    arr_2[ni][nj] = 1
                    if arr[ni][nj] == 0:
                        check = list()
                        break
                    elif arr[ni][nj] == stone_c:
                        break
                    else:
                        a = [ni, nj]
                        check.append(a)
            for c in check:
                change_stones.append(c)

        print(change_stones)
        for k in range(4):
            check = list()
            for n in range(1, N):
                nx = x + (dx[k] * n)
                ny = y + (dy[k] * n)
                if 0 <= nx < N and 0 <= ny < N:
                    print(nx, ny)
                    arr_2[nx][ny] = 1
                    if arr[nx][ny] == 0:
                        check = list()
                        break
                    elif arr[nx][ny] == stone_c:
                        break
                    else:
                        a = [nx, ny]
                        check.append(a)
            for c in check:
                change_stones.append(c)
        print(change_stones)
        change(change_stones, stone_c)
        print(arr_2)
        print(arr)


    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                black += 1
            elif arr[i][j] == 2:
                white += 1


    print('#{} {} {}'.format(t+1, black, white))



