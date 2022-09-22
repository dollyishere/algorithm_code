def bomb_search():
    global bomb_count

    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'O':
                bomb_count[i][j] -= 1
            else:
                pass


def bomb_set():
    global arr
    global bomb_count

    for i in range(R):
        for j in range(C):
            if arr[i][j] == '.':
                arr[i][j] = 'O'
                bomb_count[i][j] = 2
            else:
                bomb_count[i][j] -= 1

def bomb_boom():
    global arr
    global bomb_count

    for i in range(R):
        for j in range(C):
            if arr[i][j] == '.':
                pass

            elif bomb_count[i][j] != 0:
                bomb_count[i][j] -= 1
                
            elif bomb_count[i][j] == 0:
                arr[i][j] = '.'
                bomb_count[i][j] = 'x'

                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < R and 0 <= nj < C:
                        if bomb_count[ni][nj] == 0:
                            pass
                        else:
                            arr[ni][nj] = '.'
                            bomb_count[ni][nj] = 'x'


# R은 직사각형 격자판의 세로, C는 가로 길이, N는 초를 뜻함
R, C, N = map(int, input().split())

# 현재 격자판 상황 받아주기
arr = [list(input()) for _ in range(R)]
# 폭탄 좌표와 상황을 넣어줄 리스트 생성
bomb_count = [['x'] * C for _ in range(R)]
bomb_list = list()

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

# 법칙을 보면, 초가 홀수일 때 빈 자리에 폭탄을 설치함
# 반대로 짝수 턴일 때는 설치한지 3초가 지난 폭탄이 폭발하며 십자가 형태로 흔적을 남김(해당 지역 폭탄도 함께 삭제)
# 따라서 이번 문제에서 가장 중요한 것은 '해당 폭탄이 설치된지 얼마나 지났는지'를 프로그램 내에서 파악하게 하는 것임
# 주의할 점은 폭탄 터진 후 그 폭발에 말려든 폭탄도 함께 말려들기 때문에 카운트 세기가 까다롭다는 점
# 그런데 홀수 턴이면 무조건 없는 자리에는 폭탄이 모조리 설치되니까 그냥 print해버리면 안되나?

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'O':
            bomb_count[i][j] = 2
        else:
            pass


for n in range(1, N + 1):
    if n == 1:
        bomb_search()
    elif n % 2 == 0:
        bomb_set()
    elif n % 2 == 1:
        bomb_boom()

for a in arr:
    print(''.join(a))

# for b in bomb_count:
#     print(''.join(list(map(str, b))))