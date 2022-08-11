import sys
sys.stdin = open('input.txt', 'r')


# 테스트 케이스 수만큼 반복
for t in range(10):
    # 테스트 케이스 수 받아주기
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    ladder = list()
    true = 0

    # 먼저 출발 가능한 시작점을 구해 ladder에 저장
    for a in range(100):
        if arr[0][a] == 1:
            ladder.append(a)

    # ladder의 길이를 구해줌(즉, 시도 가능한 모든 출발점의 개수를 구해줌)
    len_l = 0
    for i in ladder:
        len_l += 1

    # 출발점의 개수만큼 반복
    for l in range(len_l):

    # 한 막대에서 출발한 가로선이 다른 막대를 가로질러서 연속해 이어지는 경우는 없음
    # 즉, 좌측 또는 우측에 길이 나있을 때, 굳이 1씩 이동할 필요 없이 현재 출발점의 왼쪽이나 오른쪽에 있는 출발점의 좌표값만 구해주면 되는 것임
    # 현재 출발점의 좌표를 먼저 index_l에 저장해줌
        index_l = l

    # 조회 가능한 행의 총 갯수인 100만큼 반복함
        for x in range(100):
            
    # 출발점 좌표를 y에 저장
            y = ladder[index_l]
    
    # 만약 2를 발견했다면, 원하는 값을 찾은 것이므로 true 변수에 해당 출발점의 좌표값을 저장해준 후 break
            if arr[x][y] == 2:
                true = ladder[l]
                break

    # 만약 현재 y 좌표값이 99 미만인 동시에 현재 기준 바로 우측 인덱스 값이 1이라면, 바로 우측에 있는 출발점 좌표값을 index_l에 넣어줌
    # y < 99를 걸어둔 것은 인덱스에러 방지를 위함임(만약 99일 시, y+1할 때 인덱스에러가 발생)
            elif y < 99 and arr[x][y + 1] == 1:
                index_l += 1
                
    # 만약 현재 y 좌표값이 0 초과인 동시에 현재 기준 바로 좌측 인덱스 값이 1이라면, 바로 좌측에 있는 출발점 좌표값을 index_l에 넣어줌
    # y < 99를 걸어둔 것은 좌표 혼란을 방지하기 위함임(만약 0일 시, arr[x][y - 1]할 때 해당 리스트의 -1값을 가져오게 되므로)
            elif y > 0 and arr[x][y - 1] == 1:
                index_l -= 1

    # 연산이 완료되면 정해진 형식대로 값 출력
    print('#{} {}'.format(T, true))


