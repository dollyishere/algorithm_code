# 응 93%~~~
# 대체 여기서 무슨 일이 있었던 거냐
# 달팽이 가로 세로 길이 N, 좌표를 구하기를 원하는 숫자 num을 입력받아 각각 변수에 저장
N = int(input())
num = int(input())

# 달팽이 모양의 2차원 배열을 작성
snail = [[0] * N for _ in range(N)]

# 달팽이 중심값 먼저 구해주기
mid = N // 2

# 달팽이의 중심값 1, 2, 3 먼저 바꿔주기
# 굳이 먼저 바꿔주는 이유는 이후 법칙 지정할 때 번거로움을 방지하기 위해서임
snail[mid][mid] = 1
snail[mid - 1][mid] = 2
snail[mid - 1][mid + 1] = 3

# 좌표 지정값 중 x는 mid로, y는 mid + 1로(즉, 1 값의 바로 옆에 위치하도록) 설정
x = mid
y = mid + 1

# 1, 2, 3은 이미 넣은 상태이므로 4부터 시작
cnt = 4
target = 2
trigger = 1
turn = 1

while cnt <= N ** 2:
    if turn % 2 == 1:
        for i in range(target):
            if cnt > N ** 2:
                break
            else:
                if cnt == num:
                    true = [x + 1, y + 1]

                snail[x][y] = cnt
                cnt += 1
                
                if i == target - 1:
                    trigger *= -1
                    y += trigger
                    turn += 1
                else:
                    x += trigger
    else:
        for j in range(target):
            if cnt > N ** 2:
                break
            else:
                if cnt == num:
                    true = [x + 1, y + 1]

                snail[x][y] = cnt
                cnt += 1
                
                if j == target - 1:
                    target += 1
                    x += trigger
                    turn += 1
                else:
                    y += trigger

for i in range(N):
    for j in range(N):
        if snail[i][j] == num:
            bingo = [i + 1, j + 1]
        if j == N - 1:
            print(snail[i][j])
        else:
            print(snail[i][j], end=' ')

print(' '.join(list(map(str, bingo))))