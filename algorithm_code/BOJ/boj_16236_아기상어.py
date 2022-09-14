def find_shark(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                arr[i][j] = 0
                return [i, j]

def find_eatfish(arr):
    global fishes
    for i in range(N):
        for j in range(N):
            if 0 < arr[i][j] < shark_size:
                gap = abs(i - ihere[0]) + abs(j - ihere[1])
                fishes.append([gap, arr[i][j], [i, j]])

def find_wall(arr):
    global walls
    for i in range(N):
        for j in range(N):
            if shark_size < arr[i][j]:
                walls.append([i, j])

def go_to_eat(arr):

# def sort_i(arr):
#     minv = arr[0]
#     for i in range(len(arr)):
#         for j in range(i, len(arr)):
#             if arr[i][0] < minv[0]:
        

N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]
second = 0
shark_size = 2
eat_count = 0

shark_is_here = [[0] * N for _ in range(N)]
fishes = list()
walls = list()

ihere = find_shark(sea)
shark_is_here[ihere[0]][ihere[1]] = 9

find_eatfish(sea)
fishes.sort()
print(shark_is_here)
print(fishes)