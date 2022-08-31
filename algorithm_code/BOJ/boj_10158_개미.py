w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())


'''
# 시간이 개쩔게 많이 걸리는 풀이법
# 0.12초라 시간초과 뜸

trigger_i = 1
trigger_j = 1

for _ in range(t):
    p += trigger_i
    q += trigger_j
    if p == w and q == h:
        trigger_i *= -1
        trigger_j *= -1
    elif p == 0 and q == 0:
        trigger_i *= -1
        trigger_j *= -1
    elif p == w or p == 0:
        trigger_i *= -1
    elif q == h or q == 0:
        trigger_j *= -1

print(p, q)

'''
# 인터넷 매우 참고한(...) 풀이법
# 다른 풀이법은 없을까? 퍼즐이나 수학에 가까운 느낌이 든다

i = (p + t) // w

if i % 2 == 1:
    x = w - ((p + t) % w)
else:
    x = (p + t) % w

j = (q + t) // h

if j % 2 == 1:
    y = h - ((q + t) % h)
else:
    y = (q + t) % h

print(x, y)