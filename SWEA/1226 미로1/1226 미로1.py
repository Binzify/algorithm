import sys


sys.stdin = open('input.txt')

from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))  # 튜플로 위치 저장하기
    while queue:
        x, y = queue.popleft()
        for i in range(4):  # 델타 방향 탐색하기
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로에서 갈 수 없는 범위 조건인 경우에는 무시한다.
            if nx < 1 or nx >= 14 or ny < 1 or ny >= 14:
                continue
            # 만약 벽인 경우에도 무시한다.
            if graph[nx][ny] == 1:
                continue
            # 벽이 아니거나 도착지점인 경우에는
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx, ny))
            elif graph[nx][ny] == 3:
                return 1
    return 0


for _ in range(1, 11):
    tc = int(input())
    graph = []
    x = y = 1
    for i in range(16):
        graph.append(list(map(int, input())))

    # 델타 이동 ( 상 하 좌 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 출력하기
    print(f'#{tc}', bfs(x, y))
