# 씻고 풀기 아임백 예에에

# 허얼
# 대학을 졸업한 내가...초등학생?
# 굿노트중
# 테스트 케이스 수만큼 반복할 필요는 없는데 어쨌거나 9만큼 반복은 하셔야 합니다 아이고 나죽네
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

for i in range(1<<9):
    minilist = list()
    for j in range(9):    
        if i & (1<<j):
            minilist.append(arr[j])
    if len_1(minilist) == 7:
        arr_1.append(minilist)

for n in arr_1:
    if sum_1(n) == 100:
        true = n
        break
    else:
        pass

for a in range(6):
    maxv = a
    for j in range(a + 1, 7):
        if true[maxv] > true[j]:
            maxv = j
    true[a], true[maxv] = true[maxv], true[a]

for i in true:
    print(i)
    
# 으아아
# 일단 자자....


