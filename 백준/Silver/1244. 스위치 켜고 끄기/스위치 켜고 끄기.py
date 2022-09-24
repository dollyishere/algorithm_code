# 처음으로 입력 받는 것은 스위치의 개수임. 정수 형태로 입력받음.
T = int(input())

# 다음으로 입력 받는 것은 스위치의 상태임. 모두 0(꺼짐)과 1(켜짐) 둘 중 하나로 이뤄져 있음.
# split를 이용해 리스트에 담아줌.
# 이때 굳이 정수 형태로 담아줄 필요는 없음.
switch_status = input().split()

# 다음으로 입력 받는 것은 학생의 수임.
students_number = int(input())

# 마지막으로 입력 받는 것은 학생의 성별과 학생이 받은 수임.
# 이 경우 학생의 수만큼 받아줄 필요가 있음. for 반복문을 사용함.
for student in range(students_number):

# 해당 학생의 성별, 받은 수를 입력받아 각각 변수에 넣어줌    
    sex, number = input().split()
    number = int(number)

# 성별에 따라 스위치 변경 법이 다르므로, if문을 써서 구분해줌.
# 성별이 남성인 경우 먼저 작성함.
    if sex == '1':

# 학생의 성별이 남성일 시, 해당 수의 배수에 해당하는 스위치의 상태를 변경함.
# list의 경우 0부터 시작하므로, 1을 더해준 다음 number로 나눈 나머지가 0인 경우만 변경.
        for t in range(T):
            if (t + 1) % number == 0:
                if switch_status[t] == '1':
                    switch_status[t] = '0'
                else:
                    switch_status[t] = '1'
            else:
                pass


    elif sex == '2':
        x, y = 0, 0
        num = number - 1
        n = 1

        while True:
            if num - n < 0 or num + n > (T - 1):
                break

            elif switch_status[num - n] == switch_status[num + n]:
                x, y = num - n, num + n
                n += 1

            else:
                break
        # number가 1일 시의 문제인가? 흠.......2일때도 문제 생길 것 같긴 한데
        # 머리가 뱅글뱅글
        # 조금만 쉬다 하자...
        if y != 0:
            for b in range(x, y + 1):
                if switch_status[b] == '1':   
                    switch_status[b] = '0'
                else:
                    switch_status[b] = '1'
        elif y == 0:
            if switch_status[number - 1] == '1':
                switch_status[number - 1] = '0'
            else:
                switch_status[number - 1] = '1'

for i in range(len(switch_status)):
    if i == (len(switch_status) - 1):
        print(switch_status[i])
    elif (i + 1) % 20 == 0:
        print(switch_status[i], end='\n')
    else:
        print(switch_status[i], end=' ')