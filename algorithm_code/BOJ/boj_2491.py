N = int(input())

numbers = list(map(int, input().split()))
count_list = list()
maxv = 0

for i in range(N - 1):
    count_list.append(numbers[i+1] -numbers[i])

cnt = 1
for i in range(N - 1):
    if (numbers[i + 1] - numbers[i]) >= 0:
        cnt += 1
        if cnt > maxv:
            maxv = cnt
    else:
        cnt = 0
# 실수;;
# 줄어드는 것도 상정해서 푸세용
# 아마 양수/홀수 여부 따져서 그냥 쭉 가는 걸로...?는 안될까...?
print(count_list)
print(maxv)