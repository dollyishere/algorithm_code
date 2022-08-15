N = int(input())
kg = [5, 3]
cnt = cnt_1 = 0
false = 0
n = N

while N == 0:

    if N % 5 == 0:
        cnt += N // 5
        break
    
    else:
        n -= 5
        cnt_1 += 1
        if (n - 5) < 5 and (n - 5) % 3 != 0:
            if n % 3 == 0:
                N = N // 3
                cnt += N // 3
                break
            else:
                false = -1
                break
        elif 
            
            

print(cnt)

    
    '''
    elif (N % 5) % 3 == 0:
        cnt += N // 5
        N = N % 5
        cnt += N // 3
        N = N % 3

    elif N % 3 == 0:
        cnt += N // 3
        N = N % 3

    else:
        cnt = -1
    '''
    


