import sys
sys.stdin = open('sample_input.txt', 'r')

# len 함수 대체
def len_1(arr):
    cnt = 0
    for a in arr:
        cnt += 1
    return cnt


# 16진수 법칙 딕셔너리 형태로 정리(나중에 16진수에서 10진수로 바꿀 때 활용할 예정)
six_t = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
}

# 테스트 케이스 총 수를 받아줌
T = int(input())

# 테스트 케이스 수만큼 반복
for t in range(T):

    # 숫자의 개수(N)와 구하고 싶은 ~번째로 큰 값(K)를 각각 받아줌
    N, K = map(int, input().split())

    # 수의 각 요소를 하나하나 별개의 요소로 취급하여 넣어줄 빈 리스트 box_number를 만들어줌
    box_number = list()

    # N개의 숫자들을 str 형태로 S에 받아줌
    S = input()

    # N만큼 반복하며 box_number에 수(s)를 추가해줌
    for s in S:
        box_number.append(s)

    # 보물상자의 뚜껑은 무조건 4변이 존재하는 사각형 형태임
    # 따라서 N값이 아무리 변동해도 한 변에는 N // 4한 수만큼 각 수들이 들어가게 됨
    # 먼저 한 변에 들어갈 숫자의 개수를 구해 num 변수에 넣어줌
    num = N // 4

    # 각 회전을 거쳐 생성될 수들을 담아줄 빈 리스트 case를 생성함
    case = list()

    # 각 수의 개수만큼 반복함(N)
    for _ in range(N):
        # for문을 두 개 써서 한 번 회전할 때마다 num만큼의 길이를 가진 4개의 문자열을 생성할 것임!
        # 밖의 for문은 N의 길이만큼 반복하지만 한번 순회할 때마다 n의 값이 num만큼 점프하도록 range를 이용해 조정할 것임
        for n in range(0, N, num):

            # 빈 문자열 check를 생성해줌
            check = ''

            # 이제 내부의 for문은 num값만큼 반복하게 함
            # box_number의 n+i 인덱스의 값을 check에 덧붙여줌
            for i in range(num):
                check += box_number[n + i]

            # 이제 num만큼의 길이를 가진 문자열 check가 완성되었음
            # 중복은 세지 말라고 하였으므로, 이 부분에서 걸러줄 것임
            # 만약 현재 형성한 check가 이미 case 내부에 존재한다면 pass, 아니면 추가해줌
            if check in case:
                pass
            else:
                case.append(check)

        # 한 회전이 끝날 때마다, 다음 회전을 위해 box_number의 맨 뒷 인덱스의 값이 box_number의 앞으로 이동해야 함
        # 여기서는 파이써닉한 방법을 이용함
        # 먼저 box_number를 pop해준 다음(이때 인덱스 미지정 했으므로 무조건 맨 뒷 값이 제외) 리스트화 시킨 것에 남은 box_number를 덧붙여줌
        box_number = [box_number.pop()] + box_number

    # 이제 우리가 구한 문자열(16진수)를 10진수로 변경해줄 것임
    # 10진수로 변경할 값을 담아줄 빈 리스트 case_num을 생성함
    case_num = list()

    # 현재 case의 길이만큼 반복함
    for i in range(len_1(case)):
        # 16진수에 제곱해줄 값을 담은 idx_n과 합계를 저장할 total 변수 차례대로 생성(둘 다 시작은 0)
        idx_n = 0
        total = 0

        # 맨 뒷 자리가 가장 낮은 수이므로 역순으로 순회함
        # 이때 문자열의 길이는 무조건 num 값이므로 range에 잘 활용할 것
        # 미리 만들어두었던 딕셔너리를 활용하여 case[i][j]에 해당하는 값을 key로 가진 value를 불러와 해당 자릿수에 맞게 16 제곱한 값과 곱해줌
        # 연산이 끝날 때마다 idx_n에 1씩 추가함(어차피 바깥 for이 다음 회차로 넘어갈 때마다 값은 0으로 초기화 되기에 신경 ㄴㄴ)
        for j in range(num - 1, -1, -1):
            total += six_t[case[i][j]] * (16 ** idx_n)
            idx_n += 1

        # 해당하는 case의 문자열의 모든 자릿수를 순회하여 16 제곱하여 total에 더한 총합(즉, 10진수로 전환시킨 값)을 case_num에 추가해줌
        case_num.append(total)

    # case_num에 들어있는 값을 선택 정렬을 이용함
    # 병합 정렬을 이용하는 게 매우 나을 것 같긴 한데 이때는 기억이 안나서리...
    for i in range(len_1(case_num)):
        maxv = i
        for j in range(i + 1, len_1(case_num)):
            if case_num[maxv] < case_num[j]:
                maxv = j
        case_num[i], case_num[maxv] = case_num[maxv], case_num[i]

    # 모든 연산이 끝나면 지정된 조건대로 값 출력
    # 이때 파이썬 규칙을 따라 K에 -1을 해줘야 정확한 값을 도출하는 것이 가능함!
    print('#{} {}'.format(t+1, case_num[K - 1]))

