N = int(input())
maxv = 0
case = list()

for i in range(N, N // 2 - 1, -1):
    arr = [N, i]
    cnt = 2
    j = 1
    while True:
        num = arr[j - 1] - arr[j]
        if num < 0:
            if cnt > maxv:
                maxv = cnt
                case = arr
            break
        else:
            arr.append(num)
            cnt += 1
            j += 1

print(maxv)
case = list(map(str, case))
print(' '.join(case))