# 씻고 풀기 아임백 예에에

# 허얼
# 대학을 졸업한 내가...초등학생?
# 굿노트중
# 테스트 케이스 수만큼 반복할 필요는 없는데 어쨌거나 9만큼 반복은 하셔야 합니다 아이고 나죽네

arr_1 = [0] * 9
arr_2 = [0] * 36

for i in range(9):
    arr_1[i] = int(input())

for x in range(8, 0, -1):
    for y in range(0, x):
        if arr_1[y] > arr_1[y + 1]:
            arr_1[y], arr_1[y + 1] = arr_1[y + 1], arr_1[y]

# 으아아
# 일단 자자....




print(arr_1)
print(arr_2)
