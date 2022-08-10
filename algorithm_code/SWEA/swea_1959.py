# 테스트 케이스 개수 받아오기
T = int(input())
# 합계 답을 담을 빈 리스트 만들기
lista = []
# While용 += 만들기
plus = 0

for i in range(T):
    # 테스트 케이스 때마다 각 리스트 길이 새로 받음
    N, M = list(map(int, input().split()))

    # 각 리스트 정수형으로 변형한 후, 리스트로 다시 재구성함
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 각 리스트 길이를 비교하고, 더 큰 쪽을 big, BIG 변수에, 더 작은 쪽을 small, SMALL(대문자 쪽이 리스트) 변수에 넣어줌
    if N - M > 0:
        big = N
        small = M
        BIG = A
        SMALL = B
    else:
        big = M
        small = N
        SMALL = A
        BIG = B

    # f 크기 만큼 각 리스트를 번갈아 비교가 가능함
    f = (big - small) + 1

    # 길이가 더 긴 리스트 - 길이가 더 짧은 리스트의 횟수만큼 비교할 수 있음
    # 람다를 이용해 지정된대로 계산한 값을 담은 리스트를 만들어주고, 해당 리스트의 합계값을 lista에 담아줌
    for x in range(0, f):
        product = list(map(lambda a, b: a*b, BIG[x:x+small], SMALL))
        while True:
            for y in product:
                plus += y
            lista.append(plus)
            plus = 0
            break
    
    # 해당 테스트 케이스의 회차와 리스트 순회하면서 최대값(즉, lista에 담긴 최대값)을 출력해줌
    print(f'#{i + 1} {max(lista)}')
    # 다음 회차를 위해 lista 초기화
    lista = []