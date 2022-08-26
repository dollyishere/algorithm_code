import sys
sys.stdin = open('sample_input(1).txt', 'r')

# len 함수 대체
def len_1(arr):
    cnt = 0
    for a in arr:
        cnt += 1
    return cnt

# 사이에 있는 돌 색 바꿔주는 로직을 함수화
def change(c, color):
    global arr
    for a in c:
        i, j = a[0], a[1]
        arr[i][j] = color

# 테스트 케이스 총 수 입력
T = int(input())

# 테스트 케이스 반복
for t in range(T):

    # 보드 한 변의 길이(N)와 플레이어가 돌을 놓는 횟수(M)을 각각 받아줌
    N, M = map(int, input().split())

    # 2차원 배열 형태로 각 칸에 0이 들어가 있는 보드를 만들어줌
    # 이때 편의를 위해 원래 주어진 길이에서 상하좌우로 1씩 늘려줌(그래서 2, 2)
    arr = [[0] * (N + 2) for _ in range(N + 2)]

    # 이후 정답 출력을 위해 검은 돌과 흰 돌의 수를 담아줄 변수 black, white 각각 생성(초기값 0)
    black = 0
    white = 0

    # 판에 먼저 지시한대로 돌 배치한 후에 시작
    # 어차피 우리는 임의로 인덱스를 1씩 밀어줬으므로, 굳이 파이썬 규칙 신경 써서 num에 -1 해주지 않아도 괜찮음!
    # 즉, 지금 보드의 상태는 원래 보드를 0이 담긴 인덱스의 배열이 테두리를 감싸고 있는 형식임
    num = N // 2
    arr[num][num], arr[num+1][num+1] = 2, 2
    arr[num][num+1], arr[num+1][num] = 1, 1

    # 이번 문제는 8방향 모두 검증할 필요가 있으므로 델타 탐색을 통해 풀었음
    # 가로 세로
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    # 대각선
    dx = [1, 1, -1, -1]
    dy = [1, -1, 1, -1]

    # M의 크기만큼 반복
    for m in range(M):

        # 돌을 놓을 위치(x, y)와 돌의 색(stone_c)를 입력받아줌
        x, y, stone_c = map(int, input().split())

        # 먼저 돌을 지정된 위치에 배치
        arr[x][y] = stone_c

        # 바꿔야 하는 돌의 위치를 받아줄 빈 리스트 change_stones를 생성
        change_stones = list()

        # 이번 문제에서는 상하좌우는 물론 각 대각선 방향을 검증해야 함
        # 델타 탐색을 이용
        # 이 경우 검증할 칸 수가 명확히 정해져 있지는 않지만, 보드 끝까지 검증하다 만약 해당 값이 지정 범위에서 벗어나면 바로 아웃시킴
        # 만약 해당 값이 보드 안에 들어 있다면, 그 값이 0인지, 아니면 현재 돌의 색과 같은지, 아니면 색이 다른지를 검증해야 함

        # 먼저 상하좌우 탐색
        # 4방향 탐색이므로 for문의 범위는 4로 지정
        for k in range(4):
            check = list()

            # 값 증가 범위 설정의 경우 런타임 에러 날 정도로 범위가 크지는 않아서 그냥 1부터 N+2로 지정해뒀음(문제될 시 수정)
            for n in range(1, N + 2):

                # 좌표값 ni, nj 지정
                ni = x + (di[k] * n)
                nj = y + (dj[k] * n)

                # 만약 해당 좌표가 범위 내에 있다면, 이후 연산 시작
                if 0 <= ni < N + 2 and 0 <= nj < N + 2:

                # 먼저 0일 경우, 해당 값은 의미가 없으므로 check(현재까지 구한 다른 색 돌의 좌표가 담긴 리스트)를 초기화 시킨 후, break로 빠져나옴
                    if arr[ni][nj] == 0:
                        check = list()
                        break
                # 만약 1일 경우, 그냥 break(어차피 해당하는 좌표값은 이미 check에 담겨있기 때문
                    elif arr[ni][nj] == stone_c:
                        break

                # 만약 2일 경우, 해당할 수도 있으므로 check에 해당 좌표를 담아줌.
                # 설사 바꾸면 안되는 값이더라도, 어차피 보드가 0 인덱스들로 둘러싸인 이상 알아서 차단시킬 것이기 때문에 걱정 안해도 괜찮음!
                    else:
                        a = [ni, nj]
                        check.append(a)

            # 모든 방향 탐색한 후 check에 들어 있는 값을 change_stones에 추가해줌
            for c in check:
                change_stones.append(c)

        # 대각선 4 방향 검사
        # 로직 자체는 상하좌우 검사와 같기 때문에 생략
        for k in range(4):
            check = list()
            for n in range(1, N + 2):
                nx = x + (dx[k] * n)
                ny = y + (dy[k] * n)
                if 0 <= nx < N + 2 and 0 <= ny < N + 2:
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

        # 기존에 자체 제작해뒀던 change 함수를 실행시켜줌
        # change_stones 내에 존재하는 좌표들에 들어있는 인덱스 내부 값을 현재 돌의 색인 stone_c으로 바꿔줌
        change(change_stones, stone_c)

    # arr 순회하면서 검은 돌과 흰 돌의 색을 세어줌
    for i in range(N + 2):
        for j in range(N + 2):
            if arr[i][j] == 1:
                black += 1
            elif arr[i][j] == 2:
                white += 1

    # 모든 연산을 마친 후, 형식에 맞게 현재 테스트케이스 번호와 검은 돌, 흰 돌 수를 순서대로 출력
    print('#{} {} {}'.format(t+1, black, white))



