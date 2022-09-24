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