# len, sum 함수 구현
def len_1(liter):
    cnt = 0
    for i in liter:
        cnt += 1
    return cnt

def sum_1(liter):
    total = 0
    for i in liter:
        total += i
    return(total)

arr = [int(input()) for _ in range(9)]
arr_1 = list()
true = list()

# 비트 연산자 이용해 해당 집합의 구성이 7일 시에만 저장
for i in range(1<<9):
    minilist = list()
    for j in range(9):    
        if i & (1<<j):
            minilist.append(arr[j])
    if len_1(minilist) == 7:
        arr_1.append(minilist)

# 길이 7인 집합들(리스트 형태)의 합을 구함
# 합계가 100인 리스트를 발견하면 true에 저장하고 즉시 break
for n in arr_1:
    if sum_1(n) == 100:
        true = n
        break
    else:
        pass

# 오름차순으로 정렬
for a in range(6):
    maxv = a
    for j in range(a + 1, 7):
        if true[maxv] > true[j]:
            maxv = j
    true[a], true[maxv] = true[maxv], true[a]

# 조건에 맞춰 출력
for i in true:
    print(i)
    



