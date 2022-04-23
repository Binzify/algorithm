import sys


sys.stdin = open('sample_input.txt')

from collections import deque


def bfs(sx, sy, ex, ey):  # 처음 시작지점과 끝 지점을 받는다.
    queue = deque()  # 빈 큐 리스트
    visited = [[0] * N for _ in range(N)]  # 방문표시를 위한 리스트 생성해주기

    queue.append((sx, sy))  # 시작 지점을 큐에다가 넣는다.
    visited[sx][sy] = 1  # 시작 지점을 방문표시 한다. 1부터 시작 거리 측정

    while queue:
        gx, gy = queue.popleft()  # 시작 지점을 빼서
        for i in range(4):  # 4방향 탐색하면서 큐에 넣기
            nx = gx + dx[i]
            ny = gy + dy[i]
            # 우선 조건 설정하기
            if (
                0 <= nx < N
                and 0 <= ny < N
                and graph[nx][ny] == 0
                and visited[nx][ny] == 0
            ):
                queue.append((nx, ny))
                visited[nx][ny] = visited[gx][gy] + 1
            if nx == ex and ny == ey:
                return visited[gx][gy] - 1
    return 0  # 왜 마지막 3번이 안나오나?


# 델타 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    graph = []  # bfs 를 위한 값 출력
    for i in range(N):
        graph.append(list(map(int, input())))

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 2:
                stx, sty = i, j
            if graph[i][j] == 3:
                endx, endy = i, j

    print(f'#{tc} {bfs(stx,sty,endx,endy)}')
