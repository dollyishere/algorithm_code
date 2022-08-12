N = int(input())
n = N
cnt_5 = 0
cnt_3 = 0

while True:
    if n == 1:
        break
    elif n % 5 == 0:
        cnt_5 = n // 5
        n = 1
    elif (n % 5) % 3:
        n = n % 5
        cnt_5 += 1
    elif n % 3 == 0:
        cnt_3 = n // 3
        n = 1
    else:
        break

total = cnt_3 + cnt_5

if total == 0:
    total = -1

print(total)
