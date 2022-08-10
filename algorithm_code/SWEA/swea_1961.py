T = int(input())

for t in (range(T)):
    n = int(input())
    list_numbers = list()
    list_answers_1 = list()
    list_answers_2 = list()
    list_answers_3 = list()

    for i in range(n):
        a = input().split()
        list_numbers.append(a)

    for x in range(n):
        b = ''
        for y in range(n - 1, -1 , -1):
            b += list_numbers[y][x]
        list_answers_1.append(b)


    for x in range(n - 1, -1 , -1):
        b = ''
        for y in range(n - 1, -1 , -1):
            b += list_numbers[x][y]
        list_answers_2.append(b)

    for x in range(n - 1, -1 , -1):
        b = ''
        for y in range(n):
            b += list_numbers[y][x]
        list_answers_3.append(b)

    print(f'#{t + 1}')
    for i in range(n):
        print(list_answers_1[i], list_answers_2[i], list_answers_3[i], sep=' ')