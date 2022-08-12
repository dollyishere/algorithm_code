import sys
sys.stdin = open('sample_input.txt' , 'r')

# 테스트 케이스 수 받아주기
T = int(input())

# 테스트 케이스 수만큼 반복
for t in range(T):
    # 총 색칠 횟수 받아주기
    N = int(input())

    # 총 색칠 횟수만큼 입력 받아주기
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 색칠을 적용할 빈 박스(10x10) 만들어주기
    box = [[0] * 10 for _ in range(10)]

    # 색칠 별로 구분할 변수(리스트, 숫자 변수) 만들어주기
    red = list()
    blue = list()
    purple = 0

    # 각 리스트 마지막 인덱스(-1) 조회해서 빨간색/파란색 구분해서 각각 해당 리스트에 추가하기
    for a in arr:
        if a[-1] == 1:
            red.append(a)
        else:
            blue.append(a)

    # red 리스트 순회하면서 해당 박스의 범위에 드는 인덱스는 값을 1로 변경해주기
    for r in red:
        for i in range(r[0], r[2] + 1):
            for j in range(r[1], r[3] + 1):
                box[i][j] = 1

    # blue 리스트 순회하면서 해당 박스 범위 내에서 만약 값이 1인 인덱스가 있다면, purple에 1씩 추가(중복 색칠)
    for b in blue:
        for i in range(b[0], b[2] + 1):
            for j in range(b[1], b[3] + 1):
                if box[i][j] == 1:
                    purple += 1
                else:
                    pass

    # 먼저 1색(빨강) 적용되는 인덱스를 1로 바꿔주고 2돌면서 1이면 purple에 더하는?
    # 모든 연산이 끝나면 형식에 따라 값 출력하기
    print('#{} {}'.format(t+1, purple))
