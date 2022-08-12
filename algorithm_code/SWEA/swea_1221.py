# 1221_GNS
# 2022-08-12

import sys
sys.stdin = open('GNS_test_input.txt' , 'r')

# 테스트 케이스 수 받아주기
T = int(input())

# 테스트 케이스 수만큼 반복
for t in range(T):
		# 테스트 케이스 번호, 테스트 케이스 길이 모두 받아줌
    case_1, len_c = input().split()
    len_c = int(len_c)
    numbers = list(input().split())
		
		# 0~9를 나타내는 단어를 담은 list를 만들어준 후, 임의로 딕셔너리를 만들어줌
    numbers_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    numbers_dict = dict()
    
		# 테스트 케이스를 순회하면서 만약 numbers_list의 값과 같다면, cnt에 1씩 더해준 후 numbers_list for문 끝나기 전에 해당 단어를 key, cnt를 value로 하여 numbers_dict에 저장함
    for i in numbers_list:
        cnt = 0
        for j in range(len_c):
            if numbers[j] == i:
                cnt += 1
        numbers_dict[i] = cnt
		
		# 테스트 케이스 출력한 후, 문제에서 원하는 대로 작은 수부터 정렬된 문자열 출력
    print(case_1)
    for i in numbers_dict:
        for j in range(numbers_dict[i]):
            if j == (numbers_dict[i] - 1):
                print(i)
            else:
                print(i, end=' ')