def virus(v):
    global visited
    global stack
    global total
    visited.append(v)
    for w in computers_line[v]:
        if w not in visited:
            total += 1
            virus(w)


N = int(input())
lines = int(input())
computers = [list(map(int, input().split())) for _ in range(lines)]
computers_line = [[] for _ in range(N + 1)]

for c in computers:
    computers_line[c[0]].append(c[1])
    computers_line[c[1]].append(c[0])

visited = []
stack = []
total = 0

if len(computers_line[1]) == 0:
    pass
else:
    virus(1)

print(total)