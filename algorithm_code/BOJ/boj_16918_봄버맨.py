# 폭탄 설치를 위한 함수 bomb_set을 생성
def bomb_set():
    # 현재 폭탄 설치 상황을 나타내는 arr 및 bomb_count를 global화 하여 함수 내에서 수정할 수 있도록 함
    global arr
    global bomb_count

    # 2중 for문을 이용해 arr내 모든 좌표를 조회
    # 만약 현 좌표값이 '.'이라면, 폭탄을 설치해주고('O'로 해당 좌표 값을 변경해주고), bomb_count의 해당 좌표 값을 2로 지정해줌
    # 굳이 3이 아니라 2로 지정하는 이유는, 폭탄을 터트리는 함수를 지정하는 시점에서 현재 값이 0일 경우 폭탄을 터트리도록 하기 위해서임
    # 그 때 기준 값을 1로 지정하면 여기서는 3으로 넣어도 괜찮을 것임!
    for i in range(R):
        for j in range(C):
            if arr[i][j] == '.':
                arr[i][j] = 'O'
                bomb_count[i][j] = 2
    # 만약 이미 폭탄이 설치되어 있는 상태라면, count의 값을 1씩 감소(시간 경과)
            else:
                bomb_count[i][j] -= 1

# 폭탄을 터트릴 때를 위한 함수 bomb_boom을 생성
def bomb_boom():
    # 현재 폭탄 설치 상황을 나타내는 arr 및 bomb_count를 global화 하여 함수 내에서 수정할 수 있도록 함
    global arr
    global bomb_count

    # 2중 for문을 이용해 arr내 모든 좌표를 조회
    for i in range(R):
        for j in range(C):

            # 만약 현 좌표 값이 '.'이라면, 폭탄이 설치되지 않은 것이므로 pass
            # 사실 이미 이 이전 단계에서 폭탄이 모든 arr에 설치된 상태이므로 이 구절은 제외해도 괜찮을 듯?
            # 제외해봤더니 런타임에러(typeerror) 뜨는 걸 보면 초기값 'x'로 둔 게 잘못인듯...
            if arr[i][j] == '.':
                pass
            
            # 만약 폭탄 카운트가 0이 아닐 시, 시간 경과를 나타내기 위해 bomb_count 리스트의 해당 좌표 값에서 1씩 빼줌
            elif bomb_count[i][j] != 0:
                bomb_count[i][j] -= 1
            
            # 만약 bomb_count[i][j]가 0일 시, 폭탄이 폭발함!
            # arr의 해당 좌표 값을 '.'으로 변경해준 후, bomb_count의 해당 좌표 값도 'x'로 변경해줌
            elif bomb_count[i][j] == 0:
                arr[i][j] = '.'
                bomb_count[i][j] = 'x'

                # 해당 폭탄을 기준으로 4방향 1칸씩 조회하며 폭탄을 터트려줘야 함!
                # 여기서는 델타탐색을 진행
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]

                    # 먼저 해당 값이 범위 내인지를 조회한 후, 값 변경을 실시함
                    if 0 <= ni < R and 0 <= nj < C:
                        # 만약 해당 좌표의 bomb_count 값이 0이라면, 그 폭탄도 이번 회차에서 터져야 하는 폭탄임
                        # 이 폭탄을 터트렸다가는 이후 계산에서 문제가 되므로, 일단 터트리지 않고 넘어감
                        if bomb_count[ni][nj] == 0:
                            pass
                        # 만약 이번에 터지지 않는 폭탄이라면, 터트림
                        else:
                            arr[ni][nj] = '.'
                            bomb_count[ni][nj] = 'x'


# R은 직사각형 격자판의 세로, C는 가로 길이, N는 초를 뜻함
R, C, N = map(int, input().split())

# 현재 격자판 상황 받아주기
arr = [list(input()) for _ in range(R)]

# 현재 폭탄 좌표와 상황(설치된지 몇초 지났는지)을 넣어줄 리스트 bomb_count 생성
# 만약 폭탄이 설치되지 않은 상태라면, 'x'로 지정(기초값으로, 0일 때와의 구분을 위함임)
bomb_count = [['x'] * C for _ in range(R)]

# 델타 탐색 진행을 위한 좌표 지정 리스트 di, dj를 각각 생성
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

# 법칙을 보면, 초가 홀수일 때 빈 자리에 폭탄을 설치함
# 반대로 짝수 턴일 때는 설치한지 3초가 지난 폭탄이 폭발하며 십자가 형태로 흔적을 남김(해당 지역 폭탄도 함께 삭제)
# 따라서 이번 문제에서 가장 중요한 것은 '해당 폭탄이 설치된지 얼마나 지났는지'를 프로그램 내에서 파악하게 하는 것임
# 주의할 점은 폭탄 터진 후 그 폭발에 말려든 폭탄도 함께 말려들기 때문에 카운트 세기가 까다롭다는 점
# 그런데 짝수 턴이면 무조건 없는 자리에는 폭탄이 모조리 설치되니까 그냥 print해버리면 안되나?

# 먼저 2중 for문을 통해 arr의 각 좌표를 조회하며 초기 폭탄 설치 상황을 파악하고, bomb_count에 반영해줌
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'O':
            bomb_count[i][j] = 2
        else:
            pass

# N(초) 만큼 for문을 통해 반복
# 만약 1초째라면, 그 때는 봄버맨이 아무 행동도 하지 않고 시간만 경과됨
# 따라서 arr에서 폭탄이 설치된 좌표를 조회하며 bomb_count 해당 좌표 값에서 1씩 빼줌
for n in range(1, N + 1):
    if n == 1:
        for i in range(R):
            for j in range(C):
                if arr[i][j] == 'O':
                    bomb_count[i][j] -= 1
                else:
                    pass
    # 만약 n이 짝수라면, 폭탄을 설치함
    elif n % 2 == 0:
        bomb_set()
    # 만약 n이 홀수라면, 폭탄을 터트림
    elif n % 2 == 1:
        bomb_boom()

# 모든 연산이 끝난 후, 직사각형 격자의 현 상황을 join 함수를 이용해 출력함
for a in arr:
    print(''.join(a))
