# 2중 for문 아마도 불가
# 어떻게 하냐 젠장~~~

N = int(input())
houses = list(map(int, input().split()))
# position = [0] * (max(houses) + 1)

# for h in range(len(houses)):
#     position[houses[h]] = houses[h]
houses.sort()

total = 0
for h in houses:
    total += h

middle = (N - 1) // 2

print(houses[middle])

# middle = total // N
# print(houses)

# middle = (max(houses) + min(houses)) // 2

# minv = 100001
# check_index = 100001
# for h in houses:
#     check = abs(h - middle)
#     if check == minv:
#         if h < check_index:
#             minv = check
#             check_index = h
#         else:
#             pass
#     elif check < minv:
#         minv = check
#         check_index = h

# print(check_index)

# for h in range(max(houses), min(houses) - 1, -1):
