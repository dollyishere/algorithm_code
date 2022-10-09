N = int(input())
students = list(map(int, input().split()))

standing = [0]

for i in range(N):
    if students[i] == 0:
        standing += [i + 1]
    else:
        change = i - (students[i] - 1)
        standing = standing[:change] + [i+1] + standing[change:]
    print(standing)

for j in range(len(standing)):
    if standing[j] == 0:
        pass
    elif j == len(standing) - 1:
        print(standing[j])
    else:
        print(standing[j], end=' ')