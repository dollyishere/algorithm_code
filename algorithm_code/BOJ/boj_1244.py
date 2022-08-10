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

# 해당 학생의 성별, 받은 수를 입력받아 각각 변수에 넣어줌. 
    gender, number = input().split()
    number = int(number)

# 성별에 따라 스위치 변경 법이 다르므로, if문을 써서 구분해줌.
# 성별이 남성인 경우 먼저 작성함.
    if gender == '1':

# 학생의 성별이 남성일 시, 해당 수의 배수에 해당하는 스위치의 상태를 변경함.
# list의 경우 0부터 시작하므로, 1을 더해준 다음 number로 나눈 나머지가 0인 경우(즉, 받은 수의 배수일 경우)만 변경.
        for t in range(T):
            if (t + 1) % number == 0:
                if switch_status[t] == '1':
                    switch_status[t] = '0'
                else:
                    switch_status[t] = '1'
            else:
                pass

# 학생의 성별이 여성일 시, 해당 수를 기준으로 대칭되게 위치한 각 인덱스의 value 값이 일치하고, 가장 많은 수의 스위치를 바꿀 수 있어야 함
# 먼저 임의의 변수 x, y를 만들어줌. 숫자를 담을 것이기에 임의로 정수 0 값을 넣어줌.
    elif gender == '2':
        x, y = 0, 0
# 학생이 받은 값에 -1을 해야 기준이 되는 스위치의 인덱스에 접근할 수 있으므로 (학생이 받은 값 - 1)한 값을 저장한 변수 num을 만들어줌 
        num = number - 1
        n = 1
# while문 용 변수 n을 만들어준 후, while문을 지정해줌.
# 만약 num - n이 0 이하가 되거나, num + n 값이 T - 1(switch_status 인덱스 최고값)이 될 시 while문에서 나가도록 break문을 작성함.
        while True:
            if num - n < 0 or num + n > (T - 1):
                break

# 만약 좌우 값이 같다면, 해당 인덱스 값을 각각 x, y에 저장해준 후, 무한 루프를 피하기 위해 n에 1을 더해줌
            elif switch_status[num - n] == switch_status[num + n]:
                x, y = num - n, num + n
                n += 1
# 좌우 대칭 값이 일치하지 않는 시점에서 스위치를 추가로 변경해야 할 필요는 없어지므로 break로 빠져나옴.
            else:
                break

# 만약 좌우 대칭 값이 일치하는 경우가 1건이라도 있었다면, 해당 범위 만큼 스위치의 값을 변경해줌.
        if y != 0:
            for b in range(x, y + 1):
                if switch_status[b] == '1':   
                    switch_status[b] = '0'
                else:
                    switch_status[b] = '1'

# 만약 1건도 없었다면, 해당 인덱스 값만 변경해줌.
        elif y == 0:
            if switch_status[number - 1] == '1':
                switch_status[number - 1] = '0'
            else:
                switch_status[number - 1] = '1'

# 출력 시, 스위치 개수가 20 이상일 경우 나눠서 출력해줘야 하기에 해당 경우를 상정해서 출력문을 작성함.
# 한 칸씩 띄워져야 하므로 end=' '를 이용함.
for i in range(len(switch_status)):
    if i == (len(switch_status) - 1):
        print(switch_status[i])
    elif (i + 1) % 20 == 0:
        print(switch_status[i], end='\n')
    else:
        print(switch_status[i], end=' ')