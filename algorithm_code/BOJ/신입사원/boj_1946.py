# 시간 초과와 틀렸습니다를 정확히 9번 반복한 후 로직 구글링 했습니다...언젠가 다시 풀어야 합니다...

import sys

# 테스트 케이스 수 받아주기
T = int(sys.stdin.readline())

# 테스트 케이스 수만큼 반복
for t in range(T):
    N = int(sys.stdin.readline())

    applicants = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    applicants.sort(key=lambda x: x[0])
    a = applicants[0][1]
    print(applicants)

    cnt = 0
    for j in range(N):
        if applicants[j][1] > a:
            cnt += 1
        else:
            if applicants[j][1] < a:
                a = applicants[j][1]

    total = N - cnt

    print(total)