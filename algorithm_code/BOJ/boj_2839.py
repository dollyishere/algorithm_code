N = int(input())
cnt = 0
false = 0
n = N

# while문 사용
# 먼저 3씩 뺀 다음, 빼고 난 값이 5의 배수면 나눠준 후 break
# 만약 3 미만이 될때까지 도달하지 못했다면, 3으로도 5로도 병행해서도 나눌 수 없는 것이므로 false에 값 넣어준 후 break
while True:
    if N % 5 == 0:
        cnt += N // 5
        break
    elif N < 3:
        false = -1
        break
    else:
        N -= 3
        cnt += 1

# 만약 false가 -1이라면 cnt도 의미가 없어지므로 false값 넣어줌
if false == -1:
    cnt = false            

# 조건에 맞춰서 출력
print(cnt)


