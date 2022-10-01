from collections import deque
import sys
import queue

input = sys.stdin.readline

def change_digit(string):
    wants = list()
    for s in string:
        if str(s).isdigit():
            wants.append(int(s))
        else:
            pass
    return wants


def f(v):
    global visited_list
    check = list()
    data_queue = deque()

    visited_list.append(v)
    check.append(v)
    data_queue.append(v)

    if len(true_list[v]) == 0:
        pass
    else:
        data_queue.extend(true_list[v])

    # print(queue)
    # print(check)
    while True:
        if data_queue:
            v = data_queue.pop(0)
            if data_queue != []:
                if v not in check:
                    visited_list.append(v)
                    check.append(v)
                    data_queue.extend(true_list[v])
                else:
                    pass
            else:
                if v not in check:
                    visited_list.append(v)
                    check.append(v)
                    data_queue.extend(true_list[v])
                else:
                    break
        else:
            break
    
    check_change = list()
    for c in check:
        c = change_digit(c)
        check_change.append(c)

    return check_change


N, L, R = map(int, input().split())

country = [list(map(int, input().split())) for _ in range(N)]

move = 0
true = 0

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

while True:
    if true == -1:
        break
    else:
        true_list = dict()
        for i in range(N):
            for j in range(N):
                search = []
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < N and 0 <= nj < N:
                        if L <= abs(country[i][j] - country[ni][nj]) <= R:
                            search.append(str([ni, nj]))
                true_list[str([i, j])] = search

        # print(true_list)
        visited_list = list()
        change_list = list()

        for i in true_list:
            # print(i)
            # print(visited_list)
            if i in visited_list:
                pass
            else:
                # print(i, 'i1i')
                change_list.append(f(i))
        # print(change_list)
        if len(change_list) == N*N:
            true = -1
            break
        else:
            move += 1
            for c in change_list:
                total = 0
                if len(c) <= 1:
                    pass
                else:
                    for p in c:
                        total += country[p[0]][p[1]]
                    for p in c:
                        country[p[0]][p[1]] = total // len(c)
            # print(country)

print(move)

