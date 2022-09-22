N = int(input())
kg = [5, 3]
cnt = cnt_1 = 0
false = 0
n = N

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

if false == -1:
    cnt = false            

print(cnt)