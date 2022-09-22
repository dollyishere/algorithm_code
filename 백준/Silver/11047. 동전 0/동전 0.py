N, K = map(int, input().split())
coin_list = [0] * N
cnt = 0

for n in range(N):
    coin_list[n] = int(input())

for c in range(N - 1, -1, -1):
    if coin_list[c] > K:
        pass
    elif K == 0:
        break
    else:
        cnt += K // coin_list[c]
        K = K % coin_list[c]

print(cnt)