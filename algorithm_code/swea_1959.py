T = int(input())
lista = []
plus = 0

for i in range(T):
    N, M = list(map(int, input().split()))

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N - M > 0:
        big = N
        small = M
        BIG = A
        SMALL = B
    else:
        big = M
        small = N
        SMALL = A
        BIG = B

    f = (big - small) + 1

    for x in range(0, f):
        product = list(map(lambda a, b: a*b, BIG[x:x+small], SMALL))
        while True:
            for y in product:
                plus += y
            lista.append(plus)
            plus = 0
            break

    print(f'#{i + 1} {max(lista)}')
    lista = []