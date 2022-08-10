for t in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    maxv = 0

    # 각 열 합을 구한 후 최대값인 경우 maxv에 저장
    for i in range(100):
        total = 0
        for j in range(100):
            total += arr[i][j]
        if maxv < total:
            maxv = total

    # 각 행 합을 구한 후 최대값인 경우 maxv에 저장
    for i in range(100):
        total = 0
        for j in range(100):
            total += arr[j][i]
        if maxv < total:
            maxv = total

    # 왼쪽->오른쪽 대각선 합을 구한 후 최대값인 경우 maxv에 저장
    for i in range(100):
        total = 0
        for j in range(100):
            if i == j:
                total += arr[i][j]
        if maxv < total:
            maxv = total

    # 오른쪽->왼쪽 대각선 합을 구한 후 최대값인 경우 maxv에 저장
    for i in range(100):
        total = 0
        for j in range(99, -1, -1):
            if (j + i) == 99:
                total += arr[i][j]
        if maxv < total:
            maxv = total

    # 테스트 케이스 수, 합계 중 최대값 출력
    print('#{} {}'.format(N, maxv))