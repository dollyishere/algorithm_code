# len 함수 제작
def len_1(array):
    count = 0
    for a in array:
        count += 1
    return count

# 이용 시간 수, 입실&퇴실 시간 각각 변수(N)와 리스트 형태(time_list)로 받아주기
N = int(input())
time_list = [list(map(int, input().split())) for _ in range(N)]

# time_list 내부 리스트들을 역순으로 정렬(가장 마지막에 위치한 리스트가 종료시각&시작 시간이 가장 늦음)
time_list.sort(key=lambda x: (x[0], x[1]), reverse=True)

# 이용 가능한 회의실 사용 시간을 담을 correct 리스트 생성
# 가장 늦은 종료시간과 시작시간을 가진 리스트의 시작시간을 time_check에 담아줌
correct = list()
time_check = time_list[0][0]

# for문을 이용해서 순회
# 가장 첫번째 리스트는 이미 사용하기로 결정된 것이나 마찬가지이므로 correct에 추가
for t in range(N):
    if t == 0:
        correct.append(time_list[t])
# 만약 time_check에 담긴 값보다 해당 t 인덱스에 해당하는 리스트의 종료시간이 더 늦을 경우, 회의실 이용 불가하므로 pass
    else:
        if time_list[t][1] > time_check:
            pass
# 만약 이용 가능하다면, correct에 해당 리스트 추가해준 후, time_check를 해당 리스트 시작 시간으로 변경해줌(다음 대조를 위함)
        else:
            correct.append(time_list[t])
            time_check = time_list[t][0]

# 모든 순회가 끝나면 correct의 요소의 총 합을 출력
print(len_1(correct))

'''
# 앞으로 비교(틀림)

N = int(input())
time_correct = list()
time_list = list()

for n in range(N):
    time_correct.append(list(map(int, input().split())))

time_correct.sort(key=lambda x: x[0] x[1])

for t in range(N):
    if t == 0:
        time_correct.append(time_list(t))
    elif time_correct[t - 1][0] == time_correct[t][0]:
        pass
    else:
        time_list.append(time_list(t))


for t in range(N):
    if t == N - 1:
        if time_list[t][0] >= time_check:
            time_check = time_list[t][1]
            correct.append(time_list[t])
            cnt += 1
    elif time_list[t][0] == time_list[t+1][0] and time_list[t][1] > time_list[t + 1][1]:
        pass
    elif time_list[t][0] < time_check:
        pass
    else:
        time_check = time_list[t][1]
        correct.append(time_list[t])
        cnt += 1

'''