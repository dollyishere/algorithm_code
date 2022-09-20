import sys
sys.stdin = open('sample_input.txt', 'r')

def len_i(arr):
    cnt = 0
    for _ in arr:
        cnt += 1
    return cnt

def change_it(s):
    global change_strikeout
    cnt = len_i(strikeout) - 1
    total = 0
    for c in range(len_i(s)):
        total += int(s[c]) * (3 ** cnt)
        cnt -= 1
    change_strikeout.append(total)

TC = int(input())

for tc in range(1, TC+1):
    binary = input()
    strikeout = input()
    answer = 0

    change_binary = list()
    change_strikeout = list()

    for b in range(len_i(binary) - 1, 0, -1):
        if binary[b] == '0':
            change_b = binary[:b] + '1' + binary[b+1:]
        elif binary[b] == '1':
            change_b = binary[:b] + '0' + binary[b+1:]
        
        cnt = len_i(binary) - 1
        total = 0
        for c in range(len_i(binary)):
            total += int(change_b[c]) * (2 ** cnt)
            cnt -= 1
        
        change_binary.append(total)
    
    for c in range(len_i(strikeout) - 1, -1, -1):
        if strikeout[c] == '0':
            change_c_1 = strikeout[:c] + '1' + strikeout[c+1:]
            change_c_2 = strikeout[:c] + '2' + strikeout[c+1:]
            change_it(change_c_1)
            change_it(change_c_2)
        elif strikeout[c] == '1':
            change_c_1 = strikeout[:c] + '0' + strikeout[c+1:]
            change_c_2 = strikeout[:c] + '2' + strikeout[c+1:]
            change_it(change_c_1)
            change_it(change_c_2)
        elif strikeout[c] == '2':
            change_c_1 = strikeout[:c] + '0' + strikeout[c+1:]
            change_c_2 = strikeout[:c] + '1' + strikeout[c+1:]
            change_it(change_c_1)
            change_it(change_c_2)

    
    for i in change_binary:
        if i in change_strikeout:
            answer = i

    print('#{} {}'.format(tc, answer))
        
