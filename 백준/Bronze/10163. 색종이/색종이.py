N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]
maxv = 0
color_check = list()

for p in paper:
    x, y = (p[0] + p[2]), (p[1] + p[3])
    p[2], p[3] = x, y

for i in range(N):
    for j in range(4):
        if paper[i][j] > maxv:
            maxv = paper[i][j]

arr = [[0] * (maxv + 1) for _ in range(maxv + 1)]

for n in range(1, N+1):
    for i in range(paper[n - 1][0], paper[n - 1][2]):
        for j in range(paper[n - 1][1], paper[n - 1][3]):
            if arr[i][j] != n:
                arr[i][j] = n

for n in range(1, N+ 1):
    check = 0
    for i in range(paper[n - 1][0], paper[n - 1][2]):
        for j in range(paper[n - 1][1], paper[n - 1][3]):
            if arr[i][j] == n:
                check += 1
    color_check.append(check)

# for a in arr:
#     print(a)

for c in color_check:
    print(c)