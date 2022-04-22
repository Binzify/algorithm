import sys


sys.stdin = open('input.txt')

N,M = map(int, input().split())
r,c,d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

# 0 북 1 동 2 남 3 서  => -1 서 -2 남 -3 동 -4 북
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

x = r+dr[d]
y = c+dc[d]

answer = 1  # 청소 횟수
room[r][c] = 1  # 그 자리에 위치하자마자 청소가 시작되므로
check = 0  # 방향을 왼쪽으로 몇 번 체크했는지 확인하는 변수

while 1:
    if room[x][y] == 0:
        room[x][y] = 1
        answer += 1
        check = 0
    else:  # 만약 0이 아니라 1이라면
        while 1:
            if room[r][c-1] == 0 and c-1 > 0:
                d = -1
                room[x][y] = 1
            else:


