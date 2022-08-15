# 동전 단위 총 개수(N)과 금액(K), 단위를 리스트로 받아줄 coin_list, 필요한 동전 개수를 담아줄 cnt 변수 생성
N, K = map(int, input().split())
coin_list = [0] * N
cnt = 0

# N만큼 for문을 통해 반복하면서 단위 수를 입력받아 coin_list에 넣어줌
for n in range(N):
    coin_list[n] = int(input())

# coin_list의 뒤로 갈 수록 금액이 커지고, 우리는 필요한 동전 개수를 최소화하고 싶음
# 따라서 리스트의 뒤에서부터 순회함
# 지정된 금액 K보다 큰 값은 if문을 통해 제외하고, K가 0이 된 시점에서 더 순회할 필요는 없으므로 break로 빠져나옴
# 만약 위의 두 조건에 해당되지 않는다면, cnt에 해당 단위로 나눈 값의 몫을 추가하고, K에는 나누고 남은 값을 저장함
for c in range(N - 1, -1, -1):
    if coin_list[c] > K:
        pass
    elif K == 0:
        break
    else:
        cnt += K // coin_list[c]
        K = K % coin_list[c]

# 모든 연산을 마친 후 cnt 출력
print(cnt)
