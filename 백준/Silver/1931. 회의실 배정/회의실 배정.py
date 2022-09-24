def len_1(array):
    count = 0
    for a in array:
        count += 1
    return count

N = int(input())
time_list = list()

for n in range(N):
    time_list.append(list(map(int, input().split())))

time_list.sort(key=lambda x: (x[0], x[1]), reverse=True)

correct = list()
time_check = time_list[0][0]


for t in range(N):
    if t == 0:
        correct.append(time_list[t])
    else:
        if time_list[t][1] > time_check:
            pass
        else:
            correct.append(time_list[t])
            time_check = time_list[t][0]

print(len_1(correct))