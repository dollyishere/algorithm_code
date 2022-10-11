import sys
sys.stdin = open('sample_input.txt', 'r')

# stack에 담겨 있는 좌표값을 이용해 해당하는 arr 좌표에 담겨 있는 값을 모두 합해서 돌려주는 sum_i 함수 제작
def sum_i(stack):
    total = 0
    for a in stack:
        total += arr[a[0]][a[1]]
    return total

# dfs를 함수적으로 구현(재귀 사용)
# 여기서 s는 해당하는 좌표의 값을 뜻함
def dfs(s):

    # 사실상 정답으로 출력할 minV를 global 선언해줌
    # 함수 내부에서 글로벌 변수인 minV를 만지작 거리기 위함
    global minV

    # 만약 s가 마지막 좌표([N-1, N-1])라면, 이미 목적지에 도달했다는 뜻임
    # 좌표 s를 stack에 담아주고, 위에서 만들어둔 sum_i 함수를 이용해 합을 구해 minV와 대조함
    # 만약 minV가 sum_i(stack)의 값보다 크다면, 후자의 값이 더 알맞는 값이므로 해당 값으로 바꿔줌
    # 위의 조건에 해당되지 않더라도 이후 절차는 같음
    # stack의 맨 뒷값을 pop을 통해 제거함
    if s == [N-1, N-1]:
        stack.append(s)
        if minV > sum_i(stack):
            minV = sum_i(stack)
        # pop을 써서 현재 s값을 제거해줌
        # 위 방법을 쓰는 이유는 이후 stack.pop()을 한 번 더 쓰게 되는데, 만약 여기에서 pop을 안써주면 이후 pop 과정에서 현 s좌표를 빼게 되므로 경로 탐색에 이상이 생기기 때문임
        stack.pop()
        print(stack)

    # 만약 현재 stack의 합이 minV보다 크다면, 이미 적합하지 못한 값인 게 증명됐으므로 더 이상 계산을 이어나갈 필요가 없음
    # return하는 것으로 더 이상 연산하지 못하게 막아줌(안하면 샘플 케이스 2건에서 시간초과 뜸!)
    elif sum_i(stack) > minV:
        return    
    else:
        # s는 좌표를 담아둔 리스트임
        # i, j를 각각 s[0], s[1] 값으로 지정해줌
        i, j = s[0], s[1]
        # 만약 visited에 방문기록이 찍히지 않은 좌표라면, 해당 좌표 visited에 기록해주고, stack에 s를 추가해줌
        if s not in visited:
            visited[i][j] = 1
            stack.append(s)
        # 델타 탐색 진행
        # 여기서 우리가 갈 수 있는 것은 현 좌표에서 오른쪽이거나 아래쪽일 경우에만 가능함
        # for 반복문 사용하여 2번만큼 이동
            for k in range(2):
        # 미리 만들어놓은 델타탐색용 리스트를 이용하여 ni, nj 값을 지정해준 후, 만약 둘 모두 유효값에서 벗어나지 않을 시, 해당 값을 dfs 함수에 넣고 다시 돌려줌
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    dfs([ni, nj])
            # 방문 기록을 초기화한 후, stack에서 맨 뒷 값을 pop으로 제거해줌
            # 이 시점에서 방문기록을 초기화해주는 이유는, 이후 진행할 탐색에서 해당 인덱스를 지나칠 때 차단되지 않기 위해서임
            # 또한 여기서 굳이 pop을 해주는 이유는 다음과 같음
            # 본래라면 다음 좌표로 넘어갈 때, 다수의 선택지가 있다면 그 중 하나를 먼저 선택해 이동하게 됨
            # 그 상태에서 목적한 좌표에 도달했을 시, 다시 이전 인덱스로 되돌아와서 이번에는 아직 선택하지 않은 다른 선택지를 선택하는 것이 dfs의 옳은 방식임
            # 하지만 여기서 stack의 맨 뒷값을 빼주지 않으면, 뒤로 돌아가서 다른 경로를 선택하는 방식이 사실상 봉쇄됨
            # 따라서 pop을 꼭 넣어주자!(내가 제대로 이해한 것인가........)
            visited[i][j] = 0
            stack.pop()
            print(stack)


# 테스트 케이스 수 받아줌
T = int(input())

# 테스트 케이스 수만큼 반복
for tc in range(1, T+1):
    # 격자 가로 세로 길이 N을 받아줌
    N = int(input())
    # N만큼 격자 상태를 2차원 배열 arr에 받아줌
    arr = [list(map(int,input().split())) for _ in range(N)]

    # 델타탐색용 리스트 di, dj 생성
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # 방문 기록을 남길 visited 리스트를 생성함
    visited = [[0 for _ in range(N)] for _ in range(N)]
    # 방문 경로를 기록해줄 stack을 빈 리스트로 생성
    stack = list()
    # 최소값 비교용(=정답으로 출력할) 변수 minV를 생성함
    # minV의 초기값은 사실상 정답으로 나올 수 없는(가능한 최대값) 값으로 설정함
    # 본 문제에서 모든 인덱스의 값이 10 이하이므로, 거기에 N 제곱을 곱한 값으로 설정해줬음
    minV = 10 * (N ** 2)
    # dfs 시행함(시작 좌표는 [0,0])
    dfs([0,0])

    # 모든 연산 수행 후, 현재 테스크 케이스 번호와 함께 정답을 출력함
    print('#{} {}'.format(tc, minV))