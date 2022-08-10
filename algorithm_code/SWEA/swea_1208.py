# 총 테스트 케이스는 10번이니 for문을 통해 10만큼 반복
for T in range(10):

    # 평탄화 작업 수행할 횟수(dump_count), 평탄화 대상인 상자들의 수가 각각 담긴 dump_list를 만들어서 값을 입력받음
    dump_count = int(input())
    dump_list = list(map(int, input().split()))
    
    # 평탄화 작업을 dump_count만큼 수행
    for d in range(dump_count):
    
    # .index() 메서드를 사용해 해당 리스트에서 가장 큰 값이 위치한 인덱스를 찾아준 후, 해당 값에 -1을 적용함
        dump_list[dump_list.index(max(dump_list))] -= 1
   
    # 마찬가지로 가장 작은 값이 위치한 인덱스를 찾아준 후 해당 값에 접근해 +1을 해줌
        dump_list[dump_list.index(min(dump_list))] += 1
    
    # 굳이 이런 공식을 사용한 이유는 가장 큰 값이나 가장 작은 값이 중복된 채 존재하고 있을 가능성을 염두에 둔 것임
    # .index() 메서드의 경우 가장 왼쪽에 위치한 값의 위치만 리턴해주기 때문임.

    # 평탄화 작업이 끝난 후, 현재 케이스 횟수와 최대값에서 최저값을 뺀 값을 출력해주는 것으로 끝.
    print(f'#{T + 1} {max(dump_list) - min(dump_list)}')
