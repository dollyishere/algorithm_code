def quick_sort(array):
    # 리스트가 하나 이하의 원소를 가지면 종료
    if len(array) <= 1: return array
    
    pivot, tail = array[0], array[1:]
    
    leftSide = [x for x in tail if x <= pivot]
    rightSide = [x for x in tail if x > pivot]
    
    return quick_sort(leftSide) + [pivot] + quick_sort(rightSide)

def len_1(array):
    count = 0
    for a in array:
        count += 1
    return count


N = int(input())
time = list()
time_list = list()


for n in range(N):
    time.append(list(map(int, input().split())))

time = quick_sort(time)

print(time)

for t in range(N):
    if t  == 0:
        time_list.append(time[t])
    elif time[t - 1][0] == time[t][0]:
        pass
    else:
        time_list.append(time[t])

cnt = 0
correct = list()
time_check = 0

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
'''