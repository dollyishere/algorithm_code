import sys

# 테스트 케이스 수 받아주기
T = int(sys.stdin.readline())

# 테스트 케이스 수만큼 반복
for t in range(T):
    N = int(sys.stdin.readline())

    applicants = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    applicants.sort(key=lambda x: x[0])
    a = applicants[0][1]

    cnt = 0
    for j in range(N):
        if applicants[j][1] > a:
            cnt += 1
        else:
            if applicants[j][1] < a:
                a = applicants[j][1]

    total = N - cnt

    print(total)