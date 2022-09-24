def sum_1(arr):
    total = 0
    for a in arr:
        total += a
    return total


bingo_board = [list(map(int, input().split())) for _ in range(5)]
speaker = [list(map(int, input().split())) for _ in range(5)]
check_list = list()
cnt = 0

for i in range(5):
    for j in range(5):
        check_list.append(speaker[i][j])

while True:
    cnt += 1
    for i in range(5):
        for j in range(5):
            if bingo_board[i][j] == check_list[cnt - 1]:
                bingo_board[i][j] = 0
                break

    bingo_check = 0
    for i in bingo_board:
        if sum_1(i) == 0:
            bingo_check += 1

    for i in range(5):
        check = 0
        for j in range(5):
            check += bingo_board[j][i]
        if check == 0:
            bingo_check += 1

    d = [0, 1, 2, 3, 4]

    cross_check_l = 0
    j = 0
    for i in range(5):
        if j == 4:
            cross_check_l += bingo_board[i][d[j]]
        else:
            cross_check_l += bingo_board[i][d[j]]
            j += 1

    if cross_check_l == 0:
        bingo_check += 1

    cross_check_r = 0
    for i in range(5):
        cross_check_r += bingo_board[i][d[j]]
        j -= 1

    if cross_check_r == 0:
        bingo_check += 1

    if bingo_check >= 3:
        break

print(cnt)