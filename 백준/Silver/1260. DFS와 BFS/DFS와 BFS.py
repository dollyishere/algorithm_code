# 정점 개수 N, 간선 개수 M, 탐색 시작할 정점의 번호 V
# 84%에서 인덱스에러러러어어어어어어ㅓㅇ
def dfs(v):
    global visited_dfs
    stack = []
    visited_dfs.append(v)
    if len(road[v]) == 0:
        return
    else:
        for r in range(len(road[v]) - 1 , -1, -1):
            stack.append(road[v][r])
        v = stack.pop()
    while True:
        if stack == [] and len(visited_dfs) == N:
            break
        else:
            if stack != []:
                if v not in visited_dfs:
                    visited_dfs.append(v)
                    for r in range(len(road[v]) - 1 , -1, -1):
                        stack.append(road[v][r])
                    v = stack.pop()
                    continue
                else:
                    v = stack.pop()
            else:
                if v not in visited_dfs:
                    visited_dfs.append(v)
                    for r in range(len(road[v]) - 1 , -1, -1):
                        stack.append(road[v][r])
                    v = stack.pop()
                    continue
                else:
                    break

    # 선입선출이면 stack이 아니지 않아...?
    # 사실 내가 하고 있는 건 BFS였던 건에 대해서
def bfs(v):
    global visited_bfs
    queue = []
    visited_bfs.append(v)
    if len(road[v]) == 0:
        return
    else:
        for r in range(len(road[v])):
            queue.append(road[v][r])
        v = queue.pop(0)
    while True:
        if queue == [] and len(visited_bfs) == N:
            break
        else:
            if queue != []:
                if v not in visited_bfs:
                    visited_bfs.append(v)
                    for r in range(len(road[v])):
                        queue.append(road[v][r])
                    v = queue.pop(0)
                    continue
                else:
                    v = queue.pop(0)
            else:
                if v not in visited_bfs:
                    visited_bfs.append(v)
                    for r in range(len(road[v])):
                        queue.append(road[v][r])
                    v = queue.pop(0)
                    continue
                else:
                    break


N, M, V = map(int, input().split())

# umm.............
numbers = [list(map(int, input().split())) for _ in range(M)]
road = [[] for _ in range(N + 1)]

# for문 이용해 경로 설정
# 이번 경우 양방향이라고 이미 문제에서 제시되어 있으므로 해당되는 인덱스에 다 값 추가해줌
for n in numbers:
    road[n[0]].append(n[1])
    road[n[1]].append(n[0])

for r in road:
    r.sort()

visited_dfs = list()
visited_bfs = list()

dfs(V)
bfs(V)

for d in range(len(visited_dfs)):
    if d == len(visited_dfs) - 1:
        print(visited_dfs[d])
    else:
        print(visited_dfs[d], end=' ')

for b in range(len(visited_bfs)):
    if b == len(visited_bfs) - 1:
        print(visited_bfs[b])
    else:
        print(visited_bfs[b], end=' ')
# 이게 되네.......................