import sys
sys.stdin = open('input.txt' , 'r')

# 테스트 케이스 수 받아주기
T = int(input())

# 테스트 케이스 수만큼 반복
for t in range(T):
    # N, M 값 입력 받기
    N, M = map(int, input().split())

    # 유적 상황 담은 2차원 배열 리스트 arr 만들어서 입력 받아주기
    arr = [list(map(int, input().split())) + [0] for _ in range(N)]
    arr.append([0] * (M + 1))
    
    # 유적 길이 담아줄 리스트 ruin 만들어주기
    ruins = list()

    # 행 조회하면서 연속된 값이 1이 나올 때마다 cnt에 1씩 더해주고, 0이 나오면 현 cnt 값 ruin에 저장한 후 0으로 초기화
    for i in range(N + 1):
        cnt = 0
        for j in range(M + 1):
            if arr[i][j] == 1:
                cnt += 1
            else:
                ruins.append(cnt)
                cnt = 0

    # 마찬가지로 열 조회하면서 값 ruin에 추가해주기
    for i in range(M + 1):
        cnt = 0
        for j in range(N + 1):
            if arr[j][i] == 1:
                cnt += 1
            else:
                ruins.append(cnt)
                cnt = 0
    
    # ruin에서 최고값 구해 maxv에 저장
    maxv = 0
    for r in ruins:
        if r > maxv:
            maxv = r

    # 모든 연산이 끝나면 정해진 형식대로 출력
    print('#{} {}'.format(t+1, maxv))