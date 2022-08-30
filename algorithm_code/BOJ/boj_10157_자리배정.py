C, R = map(int, input().split())
K = int(input())

arr = [[0] * R for _ in range(C)]

x = 0
y = 0
cnt = 1
trigger = 1
k = 0

for i in range(C + R - 1):
    if i % 2 == 0:
        for _ in range(R - k):
            arr[x][y] = cnt
            if cnt == K:
                a, b = x + 1, y + 1
            cnt += 1
            y += (1 * trigger)
        k += 1
        x += (1 * trigger)
        y -= (1 * trigger)

    else:
        for _ in range(C - k):
            arr[x][y] = cnt
            if cnt == K:
                a, b = x + 1, y + 1
            cnt += 1
            x += (1 * trigger)
        trigger = trigger * (-1)
        y += (1 * trigger)
        x += (1 * trigger)

if K > C * R:
    print(0)
else:
    print(a, b)
