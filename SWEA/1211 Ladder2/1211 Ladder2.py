import sys, copy


sys.stdin = open('input.txt')

# 델타이동 상, 좌, 우
dx = [-1, 0, 0]
dy = [0, -1, 1]

for _ in range(10):
    tc = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]  # 사다리
    mincnt = 100000
    max_y = 0  #  최종 정답, 출발지점을 설정함

    for i in range(100):
        cnt = 0
        x = 99
        y = 0
        arr = copy.deepcopy(ladder)
        if arr[x][i] == 1:  # 출발지 지점을 정한다.
            x = x + dx[0]
            y = i + dy[0]
            arr[x][y] = 0
            # cnt += 1
            while x != 0:  # 올라가서 확인
                if y-1 >= 0 and arr[x][y-1] == 1: # 좌측 확인하기
                    x = x+dx[1]
                    y = y+dy[1]
                elif y+1 < 100 and arr[x][y+1] == 1:  # 우측 확인하기
                    x = x+dx[2]
                    y = y+dy[2]
                else:  # 위로 올라가기
                    x = x+dx[0]
                    y = y+dy[0]
                arr[x][y] = 0
                cnt += 1
            if mincnt >= cnt:
                mincnt = cnt
                max_y = y
    print(f'#{tc} {max_y}')