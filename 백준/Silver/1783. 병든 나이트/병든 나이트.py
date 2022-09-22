N, M = map(int, input().split())
move = 1
flag = True

if N > 2:
    if M > 4:
        M -= 2
        move += 2
        
        for i in range(2):
            if flag != True:
                break
            else:
                if i % 2 == 0:
                    N -= 1
                    M -= 2
                else:
                    N += 1
                    M -= 2
                if N <= 0 or M <= 0:
                    flag = False
                else:
                    move += 1
        
        if flag:
            move += M - 1
    
    else:
        for i in range(3):
            if flag != True:
                break
            else:
                if i % 2 == 0:
                    N -= 2
                    M -= 1
                else:
                    N += 2
                    M -= 1
                if N <= 0 or M <= 0:
                    flag = False
                else:
                    move += 1
elif N == 2:
    for i in range(3):
        if flag != True:
            break
        else:
            if i % 2 == 0:
                N -= 1
                M -= 2
            else:
                N += 1
                M -= 2
            if N <= 0 or M <= 0:
                flag = False
            else:
                move += 1
else:
    pass

print(move)
