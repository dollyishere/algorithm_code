def len_1(array):
    count = 0
    for a in array:
        count += 1
    return count


N = int(input())
time_list = list()


for n in range(N):
    time_list.append(list(map(int, input().split())))

time_list.sort(key=lambda x: x[0])
print(time_list)

cnt = 0
correct = list()
time_check = time_list[-1][-1]




'''
for i in range(N):
    maxv = i
    for j in range(i + 1, N):
        if time_list[j][0] == time_list[maxv][0]:
            if time_list[j][1] < time_list[maxv][1]:
                maxv = j
            else:
                pass
        elif time_list[j][0] < time_list[maxv][0]:
            maxv = j
    time_list[i], time_list[maxv] = time_list[maxv], time_list[i]


# if (time_list[j][1] - time_list[j][0]) > (time_list[maxv][1] - time_list[maxv][0]):

print(time_list)
print(len_1(time_list))

for t in range(len_1(time_list)):
    if t == len_1(time_list) - 1:
        if time_list[t][0] >= time_check:
            time_check = time_list[t][1]
            correct.append(time_list[t])
            cnt += 1
    elif time_list[t][1] > time_list[t + 1][1] or time_list[t][0] < time_check:
        pass
    else:
        time_check = time_list[t][1]
        correct.append(time_list[t])
        cnt += 1

print(correct)
print(cnt)
'''