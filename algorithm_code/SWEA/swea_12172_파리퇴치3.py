import sys
sys.stdin = open('in1.txt', 'r')

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total = 0
    maxv = 0

    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    dx = [-1, 1, -1, 1]
    dy = [-1, -1, 1, 1]


    for i in range(N):
        for j in range(N):
            checking = list()
            check = arr[i][j]
            for k in range(4):
                for m in range(1, M):
                    ni = i + di[k] * m
                    nj = j + dj[k] * m
                    if 0 <= ni < N and 0 <= nj < N:
                        check += arr[ni][nj]
                        checking.append(arr[ni][nj])
            if check > maxv:
                maxv = check

    for i in range(N):
        for j in range(N):
            checking = list()
            check = arr[i][j]
            for k in range(4):
                for m in range(1, M):
                    ni = i + dx[k] * m
                    nj = j + dy[k] * m
                    if 0 <= ni < N and 0 <= nj < N:
                        checking.append(arr[ni][nj])
                        check += arr[ni][nj]
            if check > maxv:
                maxv = check

    print('#{} {}'.format(t+1, maxv))