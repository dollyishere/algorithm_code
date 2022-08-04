N = input()
n = input().split()

N = int(N) // 2
n = list(map(int, n))
list.sort(n)

print(n[N])