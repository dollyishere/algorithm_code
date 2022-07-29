# 빌딩의 조망권을 확보하기 위해서는 왼쪽으로 2칸, 오른쪽으로 2칸이 비어있어야 함.
# 즉, 조망권 확보한 세대가 얼마나 되는지 알고 싶은 빌딩을 기준으로 좌우 2개씩 총 4개의 빌딩의 세대 수를 구한 후, 그 중에서도 가장 높은 건물의 최고 층수가 얼마나 되는지 파악함
# 만약 현재 빌딩의 총 세대 수가 좌우 4개 빌딩 중에서 가장 높은 빌딩의 총 세대 수보다 낮다면, 조망권이 확보된 세대가 아예 없는 것임(무조건 좌우 2칸씩 확보되어야 함으로)
# 그러나 만약 그렇지 않다면, 현재 빌딩의 총 세대 수에서 주변에서 가장 높은 건물의 총 세대수 를 뺀 값이 조망권이 확보된 세대의 수가 됨

# 기본적으로 주어지는 테스트 케이스의 수는 총 10, 이 동안 반복할 필요가 있음
# 따로 입력받지 않는 값이므로 임의지정
for i in range(10):

    # 테스트 케이스의 길이를 받아옴
    T = int(input()) 

    # 조망권 확보된 세대의 수의 총합을 받아올 변수 total을 미리 지정해둠
    total = 0 
    buildings_height = list(map(int, input().split()))

    # 테스트 케이스의 맨 앞과 맨 끝이 각각 두 칸 씩 0이므로(즉, 빌딩이 없어서 비교할 필요가 없으므로), 범위를 (2, T(테스트 케이스 길이)-2)로 지정
    for t in range(2, T - 2):

    # 비교하고 싶은 빌딩(buildings_height[t])에 인접한 건물들(4개)의 세대 수를 각각 other_building(리스트)에 저장
        other_building = [buildings_height[t-2], buildings_height[t-1], buildings_height[t+1], buildings_height[t+2]]
    
    # 만약 현재 빌딩의 총 세대 수가 다른 건물보다 많다면, 조망권 확보된 세대 수만큼 total에 저장
        if buildings_height[t] > max(other_building):
            total += (buildings_height[t] - max(other_building))
    
    # 만약 아니라면, pass
        else:
            pass

    # 현재 테스트 케이스의 번호(i+1)와 조망권 확보된 세대 수 출력
    print(f'#{i+1} {total}')
