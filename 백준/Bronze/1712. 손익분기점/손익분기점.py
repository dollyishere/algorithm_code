numbers = list(map(int,input().split()))
A, B, C = numbers[0], numbers[1], numbers[2]

sales_rate = 1

if C > B:
    profit = C - B
    print((A // profit) + 1)

else:
    print(-1)
