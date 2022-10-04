# 다른 분들 풀이 '매우' 참고
# 흑흑 난 나약해

from collections import deque
import sys

input = sys.stdin.readline

# 모든 나라가 든 정사각형 배열의 가로 세로 길이를 나타내는 N, 연합 이루는 최수 기준 L, 최대 기준 R 각각 변수 설정해서 받아주기
N, L, R = map(int, input().split())

# 현재 각 나라의 상황을 담은(한 인덱스에 한 나라) 2차원 배열 country 생성
country = [list(map(int, input().split())) for _ in range(N)]

# 연합 만든 후 이동한 횟수를 기록할 변수 move 생성
move = 0

# 델타 탐색용 리스트 di, dj 생성
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

# while이 True일 때까지 반복(정확한 횟수를 우리는 알 수 없단다)
while True:
    # 반복 기록 남길 리스트 visited_list 및 탈출 변수 true 생성
    visited_list = [[0] * N for _ in range(N)]
    true = 0

    # 2중 for문을 통해 각 인덱스 돌아다니면서 bfs를 진행함
    for x in range(N):
        for y in range(N):
            # 만약 해당 인덱스가 아직 방문하지 않은 인덱스라면, deque형태로 제작한 queue에 해당 좌표를 튜플 형태로 저장(중복 제거)
            # 이때 방문 기록도 함께 남겨줌
            if visited_list[x][y] == 0:
                queue = deque([(x, y)])
                visited_list[x][y] = 1

            # 방문 기록 visited_list를 제외하고 또 하나의 리스트 search를 생성한 후 해당 bfs 실행 시 접근한 인덱스를 튜플 형태로 기록
            search = [(x, y)]
            
            # bfs 진행
            while queue:

                # 해당 문제에서는 서로 곁에 있어야 국경이 맞닿아 있음
                # 따라서 해당 인덱스의 바로 상하좌우에 위치하지 않으면 볼 필요도 없다는 것임
                # 델타 탐색 진행해서 만약 범위 내에 있고, 아직 방문하지 않은 인덱스인지 먼저 확인
                # 그 다음에는 현 인덱스의 값과 해당 인덱스의 값의 차이의 절댓값이 L 이상 R 이하라면 queue와 search에 추가하고, 방문 기록 도장 콕 찍어줌
                # 그리고 오른쪽하고 아래쪽만 봐도 되나????
                i, j = queue.popleft()
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < N and 0 <= nj < N and visited_list[ni][nj] == 0:
                        if L <= abs(country[i][j] - country[ni][nj]) <= R:
                            queue.append((ni, nj))
                            visited_list[ni][nj] = 1
                            search.append((ni, nj))

            # 만약 search의 길이가 1 초과하면, 즉 1개 이상 연합 가능하다면 연합 진행
            # true 값을 -1로 바꿔주고(아직 연합해야 할 필요 있다는 뜻임) for문으로 순회하며 평균 값으로 인덱스 값을 지정해줌
            if len(search) > 1:
                true = -1
                total = 0
                for i, j in search:
                    total += country[i][j]
                mean = total // len(search)
                for i, j in search:
                    country[i][j] = mean

    # 만약 true가 0이라면, 이동을 아예 진행할 필요가 없는 상태였던 것이므로 while문 탈출함
    if true == 0:
        break
    # 만약 true가 -1이라면, 연합 및 이동 진행된 것이므로 move에 1씩 더해줌
    else:
        move += 1

# 모든 연합 생성 및 이동 완료한 후 총 이동한 횟수 move 출력
print(move)

