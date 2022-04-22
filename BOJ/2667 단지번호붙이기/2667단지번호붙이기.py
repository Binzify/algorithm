import sys


sys.stdin = open('input.txt')

from collections import deque

def bfs(x, y):
    global town
    cnt = 1  # 집 몇 채인지 세기
    q = deque()  # 담기
    village[x][y] = '0'  # 방문표시
    q.append((x, y))  # 시작할 지점을 비어있는 큐에 넣어주기
    while q:
        gx, gy = q.popleft()  # 꺼낸 x, y 를 가지고
        for i in range(4):
            nx = gx+dx[i]  # 방향을 탐색하면서 집 찾아보기
            ny = gy+dy[i]
            if 0 <= nx < N and 0 <= ny < N and village[nx][ny] == '1':  # 인덱스 범위 벗어나지 않고 집이 있다면
                cnt += 1  # 집 수 세기
                village[nx][ny] = '0'  # 집 방문표시 하기
                q.append((nx, ny))  # 다시 큐에다가 집어넣기
    town.append(cnt)  # 센 횟수를 다 넣어주기


N = int(input())
village = [list(input()) for _ in range(N)]
town = []  # 형성된 단지 수

# 델타 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(N):
        if village[i][j] == '1':
            x, y = i, j
            bfs(x, y)

town.sort()
print(len(town))
for num in town:
    print(num)