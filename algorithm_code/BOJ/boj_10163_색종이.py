N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
maxv = 0
color_check = [0] * (N + 1)

for p in paper:
    x, y = (p[0] + p[2]), (p[1] + p[3])
    p[2], p[3] = x, y

for i in range(N):
    for j in range(4):
        if paper[i][j] > maxv:
            maxv = paper[i][j]

arr = [[0] * (maxv + 1) for _ in range(maxv + 1)]

for n in range(1, N+1):
    check = 0
    for i in range(paper[n - 1][0], paper[n - 1][2]):
        for j in range(paper[n - 1][1], paper[n - 1][3]):
            if arr[i][j] == 0:
                arr[i][j] = n
                check += 1
            elif arr[i][j] == n - 1:
                arr[i][j] = 0
                check += 1
                color_check[n-1] -= 1
            else:
                check += 1

    color_check[n] = check

# for n in range(1, N+ 1):
#
#     for i in range(paper[n - 1][0], paper[n - 1][2]):
#         for j in range(paper[n - 1][1], paper[n - 1][3]):
#             if arr[i][j] == n:
#                 check += 1
#     color_check.append(check)

# for a in arr:
#     print(a)

for c in color_check:
    print(c)
# 런타임에러런타임에러런타임에러
# 이제 보니 색종이 구역 찾는 게 가장 고역인게
# 1, 2, 3, 4 값 중에서 2번이 사실 i값이고 으아아
# 왜 돌려놓은거야야

