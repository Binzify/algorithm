import sys
sys.stdin = open('input.txt')

tc = int(input())
for t in range(1, tc+1):
    N = int(input())
    area = [[0]*10 for _ in range(10)]

    for paper in range(N):  # N개의 사각형
        sq = list(map(int, input().split()))  # 사각형에 받을 좌표와 색상
        color = sq[4]

        for move_x in range(sq[0], sq[2]+1):  # 행 기준으로 잡기  x1에서 x2 까지 이동
            for move_y in range(sq[1], sq[3]+1):  # 열 기준으로 잡기 y1에서 y2까지 이동
                area[move_x][move_y] += color

    count = 0  # area에 찍힌 넓이를 구하기
    for a in area:
        for b in a:
            if b == 3 :  # 3 : 보라색을 판단한다. 3중으로 겹치는 경우가 있으므로 3 이상을 함
                count +=1

    print(f'#{t} {count}')

