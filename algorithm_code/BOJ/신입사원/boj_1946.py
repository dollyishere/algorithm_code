import sys
sys.stdin = open('input.txt' , 'r')


def abs_1(array):
    gap = array[0] - array[1]
    if gap >= 0:
        return gap
    else:
        return - gap


T = int(input())

for t in range(T):
    N = int(input())
    applicants = [0] * N
    cnt = 0
    check = list()

    for n in range(N):
        applicants[n] = list(map(int, input().split()))
    
    applicants.sort(key=lambda x: (x[0], x[1]))
    check.append(applicants[0])

    for i in range(N):
        for j in range(i + 1, N):
            if applicants[i][0] < applicants[j][0] or applicants[i][1] < applicants[j][1]:
                check.append((applicants[i]))
            else:
                pass

    print(check)

    '''
    score = applicants[-1]
    applicants.sort(key=lambda x: x[1])
    rank = applicants[-1]

    if abs_1(score) <= abs_1(rank):
        first = score
    else:
        first = rank

    check = list()
    print(first)
    for a in applicants:
        if a[0] < first[0] or a[1] < first[1]:
            cnt += 1
            check.append(a)
        else:
            pass
    '''