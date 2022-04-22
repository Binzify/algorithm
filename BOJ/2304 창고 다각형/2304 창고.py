import sys


sys.stdin = open('input.txt')

area = [0]*1001  # L의 위치인덱스를 활용하기 위해 수를 맞추기 위해 1개 더.. 1000개로 해도됨
N = int(input())  # 기둥의 개수
for n in range(N):
    L, H = map(int,input().split())  # L = 0,0 에서부터 떨어진 거리 H = 높이
    area[L] = H  # 각 기둥의 높이를 area 내 L의 위치에 설정해둠
    # 가장 높은 기둥을 기점으로 왼쪽과 오른쪽을 나누어서 넓이를 구한다음 합한다.
    # 왼쪽넓이 + 가장높은 기둥넓이 + 오른쪽넓이 = 최종 결과값
    position = 0  # 높은 기둥의 위치가 있는 곳을 표시하기 위한 변수
    hightest = 0  # 가장 높은 기둥
    highloca = 0  # 큰 기둥이 서있는 위치 저장

    # 가장 높은 기둥 찾기
    for i in area:
        position += 1
        if hightest < i :
            hightest = i
            highloca = position

    # 왼쪽에서부터 탐색하기 (왼쪽 ~ 높은 기둥위치까지)
    left = 0
    for l in range(0, highloca):
        if area[l] == 0:
            area[l] = left
        elif area[l] != 0:
            if area[l] < left:
                area[l] = left
            if area[l] > left:
                left = area[l]

    #오른쪽에서부터 탐색 (뒤에서 큰 기둥까지)
    right = 0
    for r in range(len(area)-1, highloca-1, -1):
        if area[r] == 0:
            area[r] = right
        elif area[r] != 0:
            if area[r] > right :
                right = area[r]
            elif area[r] < right :
                area[r] = right

    result = 0  # 정리한 기둥들의 합을 결과로출력하면 된다.
    for tall in area:
        result += tall
print(result)








