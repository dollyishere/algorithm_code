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