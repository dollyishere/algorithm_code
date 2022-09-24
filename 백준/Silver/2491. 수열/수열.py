N = int(input())

numbers = list(map(int, input().split())) + [0]
maxp = 0
maxm = 0

cnt_1 = 1

for n in range(N - 1):
    if numbers[n + 1] >= numbers[n]:
        cnt_1 += 1
        if cnt_1 > maxp:
            maxp = cnt_1
    else:
        if cnt_1 > maxp:
            maxp = cnt_1
        cnt_1 = 1

cnt_2 = 1

for n in range(N - 1):
    if numbers[n + 1] <= numbers[n]:
        cnt_2 += 1
        if cnt_2 > maxm:
            maxm = cnt_2
    else:
        if cnt_1 > maxm:
            maxm = cnt_2
        cnt_2 = 1

if maxp == 0 and maxm == 0:
    print(1)
else:
    if maxm > maxp:
        print(maxm)
    else:
        print(maxp)