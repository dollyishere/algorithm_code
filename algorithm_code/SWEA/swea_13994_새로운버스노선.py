T = int(input())

for t in range(T):
    arr = [0] * 1001
    bus_list = list()
    N = int(input())

    for _ in range(N):
        bus_list.append(list(map(int, input().split())))

    for bus in bus_list:
        case, a, b = bus[0], bus[1], bus[2]
        if case == 1:
            for i in range(a, b + 1):
                arr[i] += 1
        elif case == 2:
            if a % 2 == 0:
                for i in range(a, b + 1):
                    if i % 2 == 0:
                        arr[i] += 1
            else:
                for i in range(a, b + 1):
                    if i % 2 == 1:
                        arr[i] += 1
        elif case == 3:
            if a % 2 == 0:
                for i in range(a, b + 1):
                    if i % 4 == 0:
                        arr[i] += 1
            else:
                for i in range(a, b + 1):
                    if i % 3 == 0 and i % 10 != 0:
                        arr[i] += 1

    maxv = 0
    for i in range(1001):
        if arr[i] > maxv:
            maxv = arr[i]

    print('#{} {}'.format(t+1, maxv))

# yessssssss