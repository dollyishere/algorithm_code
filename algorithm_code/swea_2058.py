N = input()
list_1 = []
i = 0
plus = 0

while i <= (len(N) - 1):
    list_1.append(N[i])
    i += 1

list_2= list(map(int, list_1))

for i in range(len(list_2)):
    plus += list_2[i]

print(plus)