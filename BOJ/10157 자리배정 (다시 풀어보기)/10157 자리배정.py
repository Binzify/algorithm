import sys
sys.stdin = open('input.txt')

c, r = map(int,input().split())  # 공연장 크기
k = int(input())  # 대기표번호
stage = [[0]*c for _ in range(r)]

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]

# 공연장 크기보다 대기표 번호가 더 큰 경우에는 무효
if c*r < k:
    print(0)
# 그렇지 않은 경우에는 좌석에 대기번호 부여하기
else:
    waiting = 0  # 번호 부여하기 위함
    x, y = r, 0  # 처음 아래 반복문을 돌 때 1을 빼고 시작할 것이고 또 인덱스 값이 5,0 4,0 .. 이런순으로 갔다가 이동하므로
    move = 0
    while waiting < k:  # 대기번호가 점점 커지다 k를 넘어서는 경우 멈추기
        while waiting < k and 0 <= x + dx[move] < r and 0 <= y+dy[move] < c:  # 세로는 r 의 범위 안에서, 가로는 r의 범위 안에서
            if stage[x+dx[move]][y+dy[move]] == 0:  # 해당 자리가 비어있다면
                x += dx[move]
                y += dy[move]
                # 우선 계속 위로 올라간다.
                waiting += 1
                stage[x][y] = waiting  # 좌석에 번호를 부여한다.
            else:  # 좌석이 이미 차있다면 멈추기
                break
        move = (move + 1) % 4

    print(x+1, r-y)


