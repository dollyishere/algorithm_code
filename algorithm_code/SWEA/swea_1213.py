import sys
sys.stdin = open('test_input.txt' , 'r', encoding='UTF-8')

# len 함수 구현
def len_1(liter):
    cnt = 0
    for i in liter:
        cnt += 1
    return cnt

# 테스트 케이스 수만큼 반복
for t in range(10):
    T = int(input())

    # 특정한 문자열의 개수를 담을 변수(count_find)를 만들어줌
    count_find = 0

    # 특정 문자열(find_1), 영어 문장(s) 입력 받아 저장
    find_1 = input()
    s = input()

    # 각각의 길이를 구해줌
    s_len = len_1(s)
    find_len = len_1(find_1)

    # 반복할 수 있는 만큼(영어 문장 길이 - 특정 문자열 길이 + 1) 반복하며 인덱싱 이용해 만약 일치하면 count_find에 1씩 더해줌
    # 아니면 그냥 pass
    for i in range(s_len - find_len + 1):
        if s[i: i + find_len] == find_1:
            count_find += 1
        else:
            pass
    
    # 연산 끝마친 후 정해진 형식대로 결과 출력
    print('#{} {}'.format(T, count_find))